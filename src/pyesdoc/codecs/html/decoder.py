# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.html.decoder.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Decodes a document from an HTML text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""



def decode(as_html):
    """Decodes a document from a html text blob.

    :param as_html: Document html representation.
    :type as_html: unicode | str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    raise NotImplementedError()
