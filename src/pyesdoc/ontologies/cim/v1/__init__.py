# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.__init__.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim v1 package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-01 16:50:10.345024.

"""
from typeset import *

try:
	import decoder
except ImportError:
	pass
import typeset



# Version identifier.
ID = '1'

# Set of supported types.
TYPES = typeset.TYPES
