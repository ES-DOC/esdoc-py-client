# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.factory.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document creation functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections
import datetime
import uuid

from pyesdoc import constants
from pyesdoc import exceptions
from pyesdoc import ontologies



def create(typeof,
           project=None,
           institute=None,
           language=None,
           source=None,
           author=None,
           uid=None,
           version=None):
    """Creates a document.

    :param class typeof: Ontology type, e.g. cim.1.software.ModelComponent.
    :param str project: Project wih which instance is associated.
    :param str institute: Institute wih which instance is associated.
    :param str language: Language wih which instance is associated.
    :param str source: Source application with which instance is associated.
    :param str author: Author wih which instance is associated.
    :param uuid.UUID uid: Document unique identifier.
    :param int version: Document version.

    :returns: A pyesdoc document instance.
    :rtype: pyesdoc object

    """
    # Validate document type.
    if typeof not in ontologies.type_info.TYPES:
        raise exceptions.InvalidDocumentTypeException(typeof)

    # Set defaults.
    if not institute:
        institute = constants.DEFAULT_INSTITUTE
    if not language:
        language = constants.DEFAULT_LANGUAGE
    if not project:
        project = constants.DEFAULT_PROJECT
    if not source:
        if institute != constants.DEFAULT_INSTITUTE:
            source = institute
        else:
            source = constants.DEFAULT_SOURCE
    if not uid:
        uid = uuid.uuid4()
    if not version:
        version = 0

    # Reformat.
    institute = unicode(institute).lower()
    language = unicode(language).lower()
    project = unicode(project).lower()
    source = unicode(source).lower()
    uid = unicode(uid)

    # Verify uid.
    try:
        uuid.UUID(uid)
    except ValueError:
        raise ValueError("Document identifiers must be UUID's.")

    # Instantiate & initialize meta info (if necessary).
    doc = typeof()
    if hasattr(doc, 'meta'):
        doc.meta.author = author
        doc.meta.id = uid
        doc.meta.version = version
        doc.meta.create_date = datetime.datetime.now()
        doc.meta.institute = institute
        doc.meta.language = language
        doc.meta.project = project
        doc.meta.source = source
        doc.meta.type = doc.__class__.type_key

    return doc


def create_notebook_output(obj):
    """Returns output for an IPython notebook.

    """
    doc = collections.OrderedDict()
    for k in sorted(obj.keys()):
        doc[k] = obj[k]

    return doc
