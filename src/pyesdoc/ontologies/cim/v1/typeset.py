# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset.py

   :copyright: @2014 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2014-06-06 13:55:48.248410.

"""

# Module imports.
from typeset_for_activity_package import *
from typeset_for_data_package import *
from typeset_for_grids_package import *
from typeset_for_misc_package import *
from typeset_for_quality_package import *
from typeset_for_shared_package import *
from typeset_for_software_package import *

import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_grids_package as grids
import typeset_for_misc_package as misc
import typeset_for_quality_package as quality
import typeset_for_shared_package as shared
import typeset_for_software_package as software

import typeset_meta         # Assigns type info.



# Module exports.
__all__ = [
    'TYPES',
    'activity',
    'data',
    'grids',
    'misc',
    'quality',
    'shared',
    'software',
    'Activity',
    'BoundaryCondition',
    'Conformance',
    'DownscalingSimulation',
    'Ensemble',
    'EnsembleMember',
    'Experiment',
    'ExperimentRelationship',
    'ExperimentRelationshipTarget',
    'InitialCondition',
    'LateralBoundaryCondition',
    'MeasurementCampaign',
    'NumericalActivity',
    'NumericalExperiment',
    'NumericalRequirement',
    'NumericalRequirementOption',
    'OutputRequirement',
    'PhysicalModification',
    'Simulation',
    'SimulationComposite',
    'SimulationRelationship',
    'SimulationRelationshipTarget',
    'SimulationRun',
    'SpatioTemporalConstraint',
    'DataContent',
    'DataDistribution',
    'DataExtent',
    'DataExtentGeographical',
    'DataExtentTemporal',
    'DataExtentTimeInterval',
    'DataHierarchyLevel',
    'DataObject',
    'DataProperty',
    'DataRestriction',
    'DataStorage',
    'DataStorageDb',
    'DataStorageFile',
    'DataStorageIp',
    'DataTopic',
    'CoordinateList',
    'GridExtent',
    'GridMosaic',
    'GridProperty',
    'GridSpec',
    'GridTile',
    'GridTileResolutionType',
    'VerticalCoordinateList',
    'CimQuality',
    'Evaluation',
    'Measure',
    'Report',
    'Calendar',
    'Change',
    'ChangeProperty',
    'Citation',
    'ClosedDateRange',
    'Compiler',
    'Daily360',
    'DataSource',
    'DateRange',
    'DocGenealogy',
    'DocMetaInfo',
    'DocReference',
    'DocRelationship',
    'DocRelationshipTarget',
    'License',
    'Machine',
    'MachineCompilerUnit',
    'OpenDateRange',
    'PerpetualPeriod',
    'Platform',
    'Property',
    'RealCalendar',
    'Relationship',
    'ResponsibleParty',
    'ResponsiblePartyContactInfo',
    'Standard',
    'StandardName',
    'Component',
    'ComponentLanguage',
    'ComponentLanguageProperty',
    'ComponentProperty',
    'Composition',
    'Connection',
    'ConnectionEndpoint',
    'ConnectionProperty',
    'Coupling',
    'CouplingEndpoint',
    'CouplingProperty',
    'Deployment',
    'EntryPoint',
    'ModelComponent',
    'Parallelisation',
    'ProcessorComponent',
    'Rank',
    'SpatialRegridding',
    'SpatialRegriddingProperty',
    'SpatialRegriddingUserMethod',
    'StatisticalModelComponent',
    'TimeLag',
    'TimeTransformation',
    'Timing',
    'DocumentSet',
]



# Supported types.
TYPES = (
    activity.Activity,
    activity.BoundaryCondition,
    activity.Conformance,
    activity.DownscalingSimulation,
    activity.Ensemble,
    activity.EnsembleMember,
    activity.Experiment,
    activity.ExperimentRelationship,
    activity.ExperimentRelationshipTarget,
    activity.InitialCondition,
    activity.LateralBoundaryCondition,
    activity.MeasurementCampaign,
    activity.NumericalActivity,
    activity.NumericalExperiment,
    activity.NumericalRequirement,
    activity.NumericalRequirementOption,
    activity.OutputRequirement,
    activity.PhysicalModification,
    activity.Simulation,
    activity.SimulationComposite,
    activity.SimulationRelationship,
    activity.SimulationRelationshipTarget,
    activity.SimulationRun,
    activity.SpatioTemporalConstraint,
    data.DataContent,
    data.DataDistribution,
    data.DataExtent,
    data.DataExtentGeographical,
    data.DataExtentTemporal,
    data.DataExtentTimeInterval,
    data.DataHierarchyLevel,
    data.DataObject,
    data.DataProperty,
    data.DataRestriction,
    data.DataStorage,
    data.DataStorageDb,
    data.DataStorageFile,
    data.DataStorageIp,
    data.DataTopic,
    grids.CoordinateList,
    grids.GridExtent,
    grids.GridMosaic,
    grids.GridProperty,
    grids.GridSpec,
    grids.GridTile,
    grids.GridTileResolutionType,
    grids.VerticalCoordinateList,
    quality.CimQuality,
    quality.Evaluation,
    quality.Measure,
    quality.Report,
    shared.Calendar,
    shared.Change,
    shared.ChangeProperty,
    shared.Citation,
    shared.ClosedDateRange,
    shared.Compiler,
    shared.Daily360,
    shared.DataSource,
    shared.DateRange,
    shared.DocGenealogy,
    shared.DocMetaInfo,
    shared.DocReference,
    shared.DocRelationship,
    shared.DocRelationshipTarget,
    shared.License,
    shared.Machine,
    shared.MachineCompilerUnit,
    shared.OpenDateRange,
    shared.PerpetualPeriod,
    shared.Platform,
    shared.Property,
    shared.RealCalendar,
    shared.Relationship,
    shared.ResponsibleParty,
    shared.ResponsiblePartyContactInfo,
    shared.Standard,
    shared.StandardName,
    software.Component,
    software.ComponentLanguage,
    software.ComponentLanguageProperty,
    software.ComponentProperty,
    software.Composition,
    software.Connection,
    software.ConnectionEndpoint,
    software.ConnectionProperty,
    software.Coupling,
    software.CouplingEndpoint,
    software.CouplingProperty,
    software.Deployment,
    software.EntryPoint,
    software.ModelComponent,
    software.Parallelisation,
    software.ProcessorComponent,
    software.Rank,
    software.SpatialRegridding,
    software.SpatialRegriddingProperty,
    software.SpatialRegriddingUserMethod,
    software.StatisticalModelComponent,
    software.TimeLag,
    software.TimeTransformation,
    software.Timing,
    misc.DocumentSet,
)
