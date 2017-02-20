
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim v2 package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
# Ontology name.
NAME = 'cim'

# Ontology Version.
VERSION = '2'

# Ontology full name.
FULL_NAME = '{}.{}'.format(NAME, VERSION)

# Ontology packag set.
import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_designing_package as designing
import typeset_for_drs_package as drs
import typeset_for_platform_package as platform
import typeset_for_science_package as science
import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_time_package as time

# Ontology class set.
from typeset_for_activity_package import Activity
from typeset_for_activity_package import AxisMember
from typeset_for_activity_package import Conformance
from typeset_for_activity_package import Ensemble
from typeset_for_activity_package import EnsembleAxis
from typeset_for_activity_package import EnsembleMember
from typeset_for_activity_package import ParentSimulation
from typeset_for_activity_package import UberEnsemble
from typeset_for_data_package import Dataset
from typeset_for_data_package import Downscaling
from typeset_for_data_package import InputDataset
from typeset_for_data_package import Simulation
from typeset_for_data_package import VariableCollection
from typeset_for_designing_package import AxisMember
from typeset_for_designing_package import DomainRequirements
from typeset_for_designing_package import EnsembleRequirement
from typeset_for_designing_package import ForcingConstraint
from typeset_for_designing_package import InitialisationRequirement
from typeset_for_designing_package import MultiEnsemble
from typeset_for_designing_package import NumericalExperiment
from typeset_for_designing_package import NumericalRequirement
from typeset_for_designing_package import OutputRequirement
from typeset_for_designing_package import Project
from typeset_for_designing_package import SimulationPlan
from typeset_for_designing_package import StartDateEnsemble
from typeset_for_designing_package import TemporalConstraint
from typeset_for_drs_package import DrsAtomicDataset
from typeset_for_drs_package import DrsEnsembleIdentifier
from typeset_for_drs_package import DrsExperiment
from typeset_for_drs_package import DrsGeographicalIndicator
from typeset_for_drs_package import DrsPublicationDataset
from typeset_for_drs_package import DrsSimulationIdentifier
from typeset_for_drs_package import DrsTemporalIdentifier
from typeset_for_platform_package import ComponentPerformance
from typeset_for_platform_package import ComputePool
from typeset_for_platform_package import Machine
from typeset_for_platform_package import Partition
from typeset_for_platform_package import Performance
from typeset_for_platform_package import StoragePool
from typeset_for_platform_package import StorageVolume
from typeset_for_science_package import Model
from typeset_for_science_package import Realm
from typeset_for_science_package import Topic
from typeset_for_science_package import TopicProperty
from typeset_for_science_package import TopicPropertySet
from typeset_for_shared_package import Citation
from typeset_for_shared_package import DocMetaInfo
from typeset_for_shared_package import DocReference
from typeset_for_shared_package import ExtraAttribute
from typeset_for_shared_package import OnlineResource
from typeset_for_shared_package import Party
from typeset_for_shared_package import QualityReview
from typeset_for_shared_package import Responsibility
from typeset_for_shared_package import TextBlob
from typeset_for_software_package import ComponentBase
from typeset_for_software_package import Composition
from typeset_for_software_package import DevelopmentPath
from typeset_for_software_package import EntryPoint
from typeset_for_software_package import Gridspec
from typeset_for_software_package import Implementation
from typeset_for_software_package import SoftwareComponent
from typeset_for_software_package import Variable
from typeset_for_time_package import Calendar
from typeset_for_time_package import DateTime
from typeset_for_time_package import DatetimeSet
from typeset_for_time_package import IrregularDateset
from typeset_for_time_package import RegularTimeset
from typeset_for_time_package import TimePeriod

# Ontology enum set.
from typeset_for_activity_package import ConformanceType
from typeset_for_data_package import DataAssociationTypes
from typeset_for_designing_package import EnsembleTypes
from typeset_for_designing_package import ExperimentalRelationships
from typeset_for_designing_package import ForcingTypes
from typeset_for_designing_package import NumericalRequirementScope
from typeset_for_drs_package import DrsFrequencyTypes
from typeset_for_drs_package import DrsGeographicalOperators
from typeset_for_drs_package import DrsRealms
from typeset_for_drs_package import DrsTimeSuffixes
from typeset_for_platform_package import StorageSystems
from typeset_for_platform_package import VolumeUnits
from typeset_for_science_package import ModelTypes
from typeset_for_shared_package import NilReason
from typeset_for_shared_package import QualityStatus
from typeset_for_shared_package import RoleCode
from typeset_for_shared_package import TextBlobEncoding
from typeset_for_software_package import CouplingFramework
from typeset_for_software_package import ProgrammingLanguage
from typeset_for_time_package import CalendarTypes
from typeset_for_time_package import PeriodDateTypes
from typeset_for_time_package import TimeUnits

import type_info
import typeset
try:
	import decoder
except ImportError:
	pass
