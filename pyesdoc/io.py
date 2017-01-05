# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.io.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document io functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import collections
import glob
import json
import operator
import os
import uuid

import pyesdoc
from pyesdoc import exceptions
from pyesdoc import ontologies
from pyesdoc.utils.convert import str_to_unicode



def get_filename(doc, encoding=None):
    """Returns document file name.

    :param object document: A pyesdoc document instance.
    :param str encoding: Document encoding.

    :returns: Document file name.
    :rtype: str

    """
    if encoding is None:
        encoding = pyesdoc.constants.ENCODING_JSON

    return '{0}_{1}_{2}.{3}'.format(doc.__class__.type_key,
                                    doc.meta.id,
                                    doc.meta.version,
                                    encoding)


def _get_filepath(io_dir, doc, encoding):
    """Returns document file path.

    """
    return os.path.join(io_dir, get_filename(doc, encoding))


def write(document, fpath, encoding=pyesdoc.constants.ENCODING_JSON):
    """Writes a document to the file system.

    :param object document: A pyesdoc document instance.
    :param str fpath: Path to I/O directory or file.
    :param str encoding: Document encoding.

    :returns: Path to created file.
    :rtype: str

    """
    if os.path.isdir(fpath):
        fpath = _get_filepath(fpath, document, encoding)
    with open(fpath, 'w') as fstream:
        fstream.write(pyesdoc.encode(document, encoding))

    return fpath


def read(fpath, encoding=None, decode=True):
    """Reads a document from file system.

    :param str fpath: Path to previously saved file.
    :param str encoding: Encoding to use during deserialization.
    :param bool decode: Flag indicating whether document will be decoded.

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Validate file path.
    if not os.path.isfile(fpath):
        raise IOError("Document file path does not exist")

    # Optionally derive encoding from file extension.
    if encoding is None:
        encoding = os.path.splitext(fpath)[1][1:]

    # Set raw content.
    with open(fpath, 'r') as fstream:
        fcontent = str_to_unicode(fstream.read())

    # Decode upon request.
    return pyesdoc.decode(fcontent, encoding) if decode else fcontent


def seek(io_dir, filter=None, latest=False):
    """Reads a document from file system.

    :param str io_dir: Path to a directory within documents exist.
    :param object filter: Filter to apply when seeking.

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    if not os.path.isdir(io_dir):
        raise ValueError("I/O directory is invalid")

    # Set search targets.
    targets = collections.defaultdict(dict)
    for uid, version, fpath in [(i.split("_")[-2], int(i.split("_")[-1].split(".")[0]), i)
               for i in glob.glob(os.path.join(io_dir, "*.*"))]:
        targets[uid][version] = fpath

    # Document collection - all.
    if filter is None and not latest:
        docs = sum([i.values() for i in targets.values()], [])
        return [read(i) for i in docs]

    # Document collection - latest.
    elif filter is None and latest:
        docs = [i[max(i.keys())] for i in targets.values()]
        return [read(i) for i in docs]

    # Document collection (typed) - all.
    elif filter in ontologies.type_info.TYPES and not latest:
        docs = sum([i.values() for i in targets.values()], [])
        docs = [i for i in docs if i.find(filter.type_key) > -1]
        return [read(i) for i in docs]

    # Document collection (typed) - latest.
    elif filter in ontologies.type_info.TYPES and latest:
        docs = [i[max(i.keys())] for i in targets.values()]
        docs = [i for i in docs if i.find(filter.type_key) > -1]
        return [read(i) for i in docs]

    # Specific document - specific version.
    elif isinstance(filter, tuple) and len(filter) == 2 and isinstance(filter[1], int):
        try:
            doc = targets[filter[0]][filter[1]]
        except AttributeError:
            return None
        else:
            return read(doc)

    # Specific document - latest version.
    elif latest:
        try:
            docs = targets[filter]
        except AttributeError:
            return None
        else:
            return read(docs[max(docs.keys())])

    # Specific document - all versions.
    else:
        try:
            docs = targets[filter]
        except AttributeError:
            return None
        else:
            return [read(i) for i in docs.values()]


def convert(fpath, to_encoding, from_encoding=None):
    """Converts a document upon file system.

    :param str fpath: Path to previously saved file.
    :param str to_encoding: Target encoding.
    :param str from_encoding: Source encoding (defaults to json).

    :returns: Path to converted pyesdoc document instance.
    :rtype: str

    """
    if not os.path.isfile(fpath):
        raise IOError("Document file path does not exist")

    document = read(fpath, from_encoding)
    fpath = "{0}.{1}".format(os.path.splitext(fpath)[0], to_encoding)

    return write(document, fpath, to_encoding)


def write_notebook_output(data):
    """Saves output from an IPython notebook.

    :param object data: IPython notebook output data.

    :returns: Path to written output.
    :rtype: str

    """
    # Format params.
    mip_era = obj['MIP_ERA'].lower()
    institute = obj['INSTITUTE'].lower()
    model = obj['MODEL'].lower()
    realm = obj['REALM'].lower()

    # Convert to ordered dictionary.
    output = collections.OrderedDict()
    for k in sorted(obj.keys()):
        output[k] = obj[k]

    # Set output file path.
    fpath = os.path.join(os.getenv('ESDOC_HOME'), 'repos/esdoc-docs')
    fpath = os.path.join(fpath, mip_era)
    fpath = os.path.join(fpath, 'models/notebooks')
    fpath = os.path.join(fpath, institute)
    fpath = os.path.join(fpath, model)
    if not os.path.isdir(fpath):
        os.makedirs(fpath)
    fpath = os.path.join(fpath, realm)

    # Write as simple JSON.
    with open("{}.json".format(fpath), 'w') as fstream:
        fstream.write(json.dumps(output, indent=4))

    return fpath
