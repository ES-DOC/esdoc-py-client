"""
.. module:: cim.v1.types.activity.numerical_experiment.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.221801.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.activity.experiment import Experiment
from pyesdoc.ontologies.cim.v1.types.shared.cim_info import CimInfo
from pyesdoc.ontologies.cim.v1.types.activity.numerical_requirement import NumericalRequirement


class NumericalExperiment(Experiment):
    """A concrete class within the cim v1 type system.

    A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.
    """

    def __init__(self):
        """Constructor"""
        super(NumericalExperiment, self).__init__()
        self.cim_info = None                         # type = shared.CimInfo
        self.description = str()                     # type = str
        self.experiment_id = str()                   # type = str
        self.long_name = str()                       # type = str
        self.requirements = []                       # type = activity.NumericalRequirement
        self.short_name = str()                      # type = str


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
        d = dict(super(NumericalExperiment, self).as_dict())
        append(d, 'cim_info', self.cim_info, False, False, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'experiment_id', self.experiment_id, False, True, False)
        append(d, 'long_name', self.long_name, False, True, False)
        append(d, 'requirements', self.requirements, True, False, False)
        append(d, 'short_name', self.short_name, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm
