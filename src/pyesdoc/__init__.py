"""
.. module:: pyesdoc.__init__.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Package initializer.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""
# Module imports.
from .defaults import (
    ESDOC_DEFAULT_LANGUAGE,
    ESDOC_DEFAULT_ENCODING
)
from .factory import (
    create
    )
from .ontologies import (
    list_types,
    is_supported
    )
from .options import (
    set as set_option,
    get as get_option,
    list as list_options
    )
from .publishing import (
    ESDOC_DOC_VERSION_LATEST,
    ESDOC_DOC_VERSION_ALL,
    publish,
    retrieve,
    unpublish
    )
from .serialization import (
    decode,
    encode,
    ESDOC_ENCODINGS,
    ESDOC_ENCODINGS_CUSTOM,
    ESDOC_ENCODING_DICT,
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML,
    METAFOR_CIM_XML_ENCODING
    )
from .utils import (
    PYESDOC_Exception,
    runtime as rt
    )
from .validation import (
    is_valid,
    validate
    )

from . import ontologies
from . import options
from . import publishing
from . import serialization
from . import utils
from . import validation


# Module exports.
__all__ = [
    'create',
    'decode',
    'encode',
    'ESDOC_DEFAULT_ENCODING',
    'ESDOC_DEFAULT_LANGUAGE',
    'ESDOC_DOC_VERSION_LATEST',
    'ESDOC_DOC_VERSION_ALL',
    'ESDOC_ENCODINGS',
    'ESDOC_ENCODINGS_CUSTOM',
    'ESDOC_ENCODING_DICT',
    'ESDOC_ENCODING_JSON',
    'ESDOC_ENCODING_XML',
    'get_option',
    'is_supported',
    'is_valid',
    'list_options',
    'list_types',
    'METAFOR_CIM_XML_ENCODING',
    'ontologies',
    'publish',
    'PYESDOC_Exception',
    'retrieve',
    'set_option',
    'unpublish',
    'validate',
]

