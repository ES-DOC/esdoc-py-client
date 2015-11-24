# -*- coding: utf-8 -*-

"""
.. module:: run_peek_document.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Peeks at a document held upon local file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options

import pyesdoc



# Define command line options.
define("file", help="Path to file to be opened.")
define("encoding", help="Encoding with which file will be opened.", default="json")


def _main():
    """Main entry point.

    """
    doc = pyesdoc.read(options.file, options.encoding)

    print pyesdoc.encode(doc, pyesdoc.ESDOC_ENCODING_JSON)


# Entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()