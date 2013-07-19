"""
.. module:: cim.v1.types.activity.activity.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.163535.

"""

# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.activity.project_type import ProjectType
from pyesdoc.ontologies.cim.v1.types.shared.responsible_party import ResponsibleParty




class Activity(object):
    """An abstract class within the cim v1 type system.

    An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.
    """
    # Abstract Base Class module.
    # N.B. - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(Activity, self).__init__()
        self.funding_sources = []                    # type = str
        self.projects = []                           # type = activity.ProjectType
        self.rationales = []                         # type = str
        self.responsible_parties = []                # type = shared.ResponsibleParty


    def as_dict(self):
        """Returns a deep dictionary representation.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'funding_sources', self.funding_sources, True, True, False)
        append(d, 'projects', self.projects, True, False, True)
        append(d, 'rationales', self.rationales, True, True, False)
        append(d, 'responsible_parties', self.responsible_parties, True, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

