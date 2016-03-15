
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.type_info.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from collections import defaultdict
import datetime
import uuid


import typeset_for_shared_package as shared
import typeset_for_data_package as data
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_misc_package as misc
import typeset_for_activity_package as activity
import typeset_for_software_package as software



# Module exports.
__all__ = [
    'PACKAGES',
    'DOCUMENT_TYPES',
    'CLASSES',
    'CLASS_PROPERTIES',
    'CLASS_OWN_PROPERTIES',
    'BASE_CLASSES',
    'BASE_CLASSED',
    'SUB_CLASSED',
    'SUB_CLASSES',
    'ENUMS',
    'CONSTRAINTS',
    'KEYS',
    'HELP'
    ]

# Supported packages.
PACKAGES = (
    shared,
    data,
    grids,
    quality,
    misc,
    activity,
    software,
)

# ------------------------------------------------
# Classes.
# ------------------------------------------------

# Supported classes.
CLASSES = (
    shared.Property,
    grids.VerticalCoordinateList,
    software.Coupling,
    data.DataStorage,
    activity.InitialCondition,
    shared.ResponsibleParty,
    software.CouplingProperty,
    software.Composition,
    software.EntryPoint,
    quality.Evaluation,
    shared.DocReference,
    software.ConnectionProperty,
    software.ProcessorComponent,
    software.ComponentLanguage,
    shared.RealCalendar,
    data.DataRestriction,
    shared.Citation,
    data.DataHierarchyLevel,
    activity.LateralBoundaryCondition,
    shared.DateRange,
    shared.Daily360,
    activity.ExperimentRelationship,
    software.SpatialRegriddingUserMethod,
    grids.GridMosaic,
    data.DataExtentTemporal,
    software.SpatialRegriddingProperty,
    data.DataExtent,
    grids.GridExtent,
    activity.Activity,
    grids.GridSpec,
    shared.Change,
    activity.SimulationRelationshipTarget,
    software.Component,
    software.SpatialRegridding,
    quality.Report,
    shared.PerpetualPeriod,
    data.DataStorageIp,
    shared.ClosedDateRange,
    activity.Conformance,
    data.DataProperty,
    activity.BoundaryCondition,
    software.ConnectionEndpoint,
    misc.DocumentSet,
    software.StatisticalModelComponent,
    software.Connection,
    activity.SpatioTemporalConstraint,
    data.DataExtentGeographical,
    grids.CoordinateList,
    software.TimeLag,
    shared.MachineCompilerUnit,
    activity.SimulationRun,
    data.DataStorageDb,
    activity.Experiment,
    software.ComponentLanguageProperty,
    data.DataExtentTimeInterval,
    quality.Measure,
    activity.ExperimentRelationshipTarget,
    shared.OpenDateRange,
    data.DataContent,
    grids.GridTile,
    software.Parallelisation,
    activity.DownscalingSimulation,
    activity.Ensemble,
    shared.ChangeProperty,
    data.DataObject,
    data.DataStorageFile,
    activity.EnsembleMember,
    activity.SimulationRelationship,
    data.DataDistribution,
    shared.DocRelationshipTarget,
    software.ComponentProperty,
    activity.Simulation,
    software.Timing,
    quality.CimQuality,
    activity.NumericalRequirement,
    activity.NumericalRequirementOption,
    activity.NumericalActivity,
    shared.DataSource,
    grids.GridProperty,
    shared.Standard,
    software.TimeTransformation,
    shared.DocGenealogy,
    software.Deployment,
    shared.Relationship,
    shared.Machine,
    software.ModelComponent,
    activity.OutputRequirement,
    grids.GridTileResolutionType,
    shared.Platform,
    data.DataTopic,
    activity.MeasurementCampaign,
    shared.Calendar,
    software.CouplingEndpoint,
    shared.DocRelationship,
    grids.SimpleGridGeometry,
    shared.DocMetaInfo,
    activity.NumericalExperiment,
    activity.PhysicalModification,
    activity.SimulationComposite,
    shared.License,
    shared.Compiler,
    software.Rank,
    shared.StandardName,
)

# Supported class properties.
CLASS_PROPERTIES = { 
    shared.Property: (
        'name',
        'value',
    ),
    grids.VerticalCoordinateList: (
        'length',
        'properties',
        'type',
        'form',
        'uom',
        'has_constant_offset',
    ),
    software.Coupling: (
        'target',
        'transformers',
        'is_fully_specified',
        'connections',
        'spatial_regriddings',
        'sources',
        'properties',
        'type',
        'purpose',
        'time_profile',
        'description',
        'time_lag',
        'time_transformation',
        'priming',
    ),
    data.DataStorage: (
        'location',
        'format',
        'modification_date',
        'size',
    ),
    activity.InitialCondition: (
        'options',
        'id',
        'description',
        'source',
        'name',
        'requirement_type',
    ),
    shared.ResponsibleParty: (
        'url',
        'role',
        'address',
        'organisation_name',
        'individual_name',
        'abbreviation',
        'email',
    ),
    software.CouplingProperty: (
        'name',
        'value',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    software.EntryPoint: (
        'name',
    ),
    quality.Evaluation: (
        'date',
        'did_pass',
        'specification',
        'specification_hyperlink',
        'title',
        'type',
        'explanation',
        'description',
        'type_hyperlink',
    ),
    shared.DocReference: (
        'id',
        'type',
        'external_id',
        'changes',
        'description',
        'name',
        'url',
        'version',
    ),
    software.ConnectionProperty: (
        'name',
        'value',
    ),
    software.ProcessorComponent: (
        'language',
        'dependencies',
        'version',
        'purpose',
        'deployments',
        'online_resource',
        'release_date',
        'parent',
        'sub_components',
        'funding_sources',
        'long_name',
        'citations',
        'properties',
        'grid',
        'meta',
        'is_embedded',
        'previous_version',
        'composition',
        'short_name',
        'responsible_parties',
        'code_access',
        'coupling_framework',
        'license',
        'description',
    ),
    software.ComponentLanguage: (
        'name',
        'properties',
    ),
    shared.RealCalendar: (
        'length',
        'description',
        'range',
    ),
    data.DataRestriction: (
        'license',
        'restriction',
        'scope',
    ),
    shared.Citation: (
        'alternative_title',
        'date_type',
        'collective_title',
        'organisation',
        'location',
        'role',
        'date',
        'title',
        'type',
    ),
    data.DataHierarchyLevel: (
        'name',
        'is_open',
        'value',
    ),
    activity.LateralBoundaryCondition: (
        'options',
        'id',
        'description',
        'source',
        'name',
        'requirement_type',
    ),
    shared.DateRange: (
        'duration',
    ),
    shared.Daily360: (
        'length',
        'description',
        'range',
    ),
    activity.ExperimentRelationship: (
        'target',
        'description',
        'direction',
        'type',
    ),
    software.SpatialRegriddingUserMethod: (
        'file',
        'name',
    ),
    grids.GridMosaic: (
        'id',
        'description',
        'is_leaf',
        'tile_count',
        'has_congruent_tiles',
        'mosaics',
        'type',
        'short_name',
        'citations',
        'long_name',
        'mosaic_count',
        'tiles',
        'mnemonic',
        'extent',
    ),
    data.DataExtentTemporal: (
        'end',
        'time_interval',
        'begin',
    ),
    software.SpatialRegriddingProperty: (
        'name',
        'value',
    ),
    data.DataExtent: (
        'geographical',
        'temporal',
    ),
    grids.GridExtent: (
        'units',
        'maximum_longitude',
        'maximum_latitude',
        'minimum_longitude',
        'minimum_latitude',
    ),
    activity.Activity: (
        'projects',
        'responsible_parties',
        'rationales',
        'funding_sources',
    ),
    grids.GridSpec: (
        'esm_exchange_grids',
        'esm_model_grids',
        'meta',
    ),
    shared.Change: (
        'description',
        'author',
        'type',
        'name',
        'date',
        'details',
    ),
    activity.SimulationRelationshipTarget: (
        'simulation',
        'target',
    ),
    software.Component: (
        'parent',
        'dependencies',
        'version',
        'deployments',
        'online_resource',
        'is_embedded',
        'description',
        'sub_components',
        'funding_sources',
        'long_name',
        'grid',
        'citations',
        'properties',
        'code_access',
        'release_date',
        'previous_version',
        'license',
        'composition',
        'responsible_parties',
        'purpose',
        'coupling_framework',
        'short_name',
        'language',
    ),
    software.SpatialRegridding: (
        'properties',
        'user_method',
        'dimension',
        'standard_method',
    ),
    quality.Report: (
        'measure',
        'evaluator',
        'evaluation',
        'date',
    ),
    shared.PerpetualPeriod: (
        'length',
        'description',
        'range',
    ),
    data.DataStorageIp: (
        'modification_date',
        'protocol',
        'location',
        'host',
        'size',
        'path',
        'format',
        'file_name',
    ),
    shared.ClosedDateRange: (
        'end',
        'duration',
        'start',
    ),
    activity.Conformance: (
        'type',
        'description',
        'requirements',
        'sources',
        'frequency',
        'is_conformant',
    ),
    data.DataProperty: (
        'value',
        'description',
        'name',
    ),
    activity.BoundaryCondition: (
        'options',
        'id',
        'description',
        'source',
        'name',
        'requirement_type',
    ),
    software.ConnectionEndpoint: (
        'instance_id',
        'properties',
        'data_source',
    ),
    misc.DocumentSet: (
        'data',
        'grids',
        'model',
        'meta',
        'platform',
        'ensembles',
        'simulation',
        'experiment',
    ),
    software.StatisticalModelComponent: (
        'language',
        'timing',
        'dependencies',
        'version',
        'purpose',
        'deployments',
        'online_resource',
        'release_date',
        'parent',
        'coupling_framework',
        'sub_components',
        'funding_sources',
        'long_name',
        'citations',
        'properties',
        'grid',
        'composition',
        'meta',
        'is_embedded',
        'previous_version',
        'type',
        'short_name',
        'responsible_parties',
        'code_access',
        'types',
        'license',
        'description',
    ),
    software.Connection: (
        'target',
        'properties',
        'spatial_regridding',
        'description',
        'priming',
        'time_lag',
        'sources',
        'time_profile',
        'transformers',
        'type',
        'time_transformation',
    ),
    activity.SpatioTemporalConstraint: (
        'date_range',
        'options',
        'spatial_resolution',
        'requirement_type',
        'id',
        'description',
        'name',
        'source',
    ),
    data.DataExtentGeographical: (
        'north',
        'east',
        'west',
        'south',
    ),
    grids.CoordinateList: (
        'length',
        'uom',
        'has_constant_offset',
    ),
    software.TimeLag: (
        'units',
        'value',
    ),
    shared.MachineCompilerUnit: (
        'compilers',
        'machine',
    ),
    activity.SimulationRun: (
        'meta',
        'spinup_simulation',
        'calendar',
        'long_name',
        'date_range',
        'control_simulation',
        'funding_sources',
        'model',
        'conformances',
        'short_name',
        'deployments',
        'inputs',
        'responsible_parties',
        'supports',
        'outputs',
        'rationales',
        'simulation_id',
        'restarts',
        'spinup_date_range',
        'description',
        'authors',
        'projects',
    ),
    data.DataStorageDb: (
        'access_string',
        'format',
        'modification_date',
        'name',
        'owner',
        'size',
        'location',
        'table',
    ),
    activity.Experiment: (
        'supports',
        'measurement_campaigns',
        'funding_sources',
        'rationales',
        'responsible_parties',
        'requires',
        'generates',
        'projects',
    ),
    software.ComponentLanguageProperty: (
        'name',
        'value',
    ),
    data.DataExtentTimeInterval: (
        'radix',
        'unit',
        'factor',
    ),
    quality.Measure: (
        'identification',
        'description',
        'name',
    ),
    activity.ExperimentRelationshipTarget: (
        'numerical_experiment',
    ),
    shared.OpenDateRange: (
        'duration',
        'end',
        'start',
    ),
    data.DataContent: (
        'purpose',
        'aggregation',
        'frequency',
        'topic',
    ),
    grids.GridTile: (
        'long_name',
        'extent',
        'geometry_type',
        'vertical_crs',
        'zcoords',
        'horizontal_resolution',
        'grid_north_pole',
        'nx',
        'discretization_type',
        'simple_grid_geom',
        'ny',
        'id',
        'area',
        'horizontal_crs',
        'is_conformal',
        'description',
        'cell_array',
        'nz',
        'is_regular',
        'cell_ref_array',
        'vertical_resolution',
        'is_terrain_following',
        'coord_file',
        'mnemonic',
        'is_uniform',
        'coordinate_pole',
        'refinement_scheme',
        'short_name',
    ),
    software.Parallelisation: (
        'processes',
        'ranks',
    ),
    activity.DownscalingSimulation: (
        'downscaling_type',
        'responsible_parties',
        'long_name',
        'meta',
        'outputs',
        'funding_sources',
        'downscaling_id',
        'projects',
        'short_name',
        'calendar',
        'supports',
        'downscaled_from',
        'inputs',
        'description',
        'rationales',
    ),
    activity.Ensemble: (
        'types',
        'responsible_parties',
        'supports',
        'long_name',
        'outputs',
        'funding_sources',
        'meta',
        'projects',
        'short_name',
        'members',
        'description',
        'rationales',
    ),
    shared.ChangeProperty: (
        'description',
        'value',
        'name',
        'id',
    ),
    data.DataObject: (
        'content',
        'purpose',
        'data_status',
        'acronym',
        'description',
        'hierarchy_level',
        'properties',
        'distribution',
        'keyword',
        'geometry_model',
        'meta',
        'source_simulation',
        'purpose',
        'extent',
        'child_object',
        'restriction',
        'parent_object',
        'citations',
        'storage',
    ),
    data.DataStorageFile: (
        'modification_date',
        'path',
        'format',
        'location',
        'file_system',
        'file_name',
        'size',
    ),
    activity.EnsembleMember: (
        'long_name',
        'responsible_parties',
        'simulation',
        'funding_sources',
        'rationales',
        'supports',
        'ensemble',
        'short_name',
        'description',
        'ensemble_ids',
        'projects',
    ),
    activity.SimulationRelationship: (
        'target',
        'description',
        'direction',
        'type',
    ),
    data.DataDistribution: (
        'access',
        'fee',
        'responsible_party',
        'format',
    ),
    shared.DocRelationshipTarget: (
        'reference',
    ),
    software.ComponentProperty: (
        'values',
        'grid',
        'sub_properties',
        'standard_names',
        'purpose',
        'intent',
        'long_name',
        'units',
        'citations',
        'short_name',
        'description',
        'is_represented',
    ),
    activity.Simulation: (
        'long_name',
        'conformances',
        'calendar',
        'supports',
        'authors',
        'spinup_date_range',
        'control_simulation',
        'funding_sources',
        'deployments',
        'responsible_parties',
        'spinup_simulation',
        'outputs',
        'restarts',
        'short_name',
        'description',
        'rationales',
        'simulation_id',
        'projects',
        'inputs',
    ),
    software.Timing: (
        'is_variable_rate',
        'end',
        'start',
        'rate',
        'units',
    ),
    quality.CimQuality: (
        'meta',
        'reports',
    ),
    activity.NumericalRequirement: (
        'options',
        'id',
        'description',
        'requirement_type',
        'name',
        'source',
    ),
    activity.NumericalRequirementOption: (
        'id',
        'description',
        'relationship',
        'sub_options',
        'name',
    ),
    activity.NumericalActivity: (
        'long_name',
        'responsible_parties',
        'short_name',
        'funding_sources',
        'supports',
        'projects',
        'description',
        'rationales',
    ),
    shared.DataSource: (
        'purpose',
    ),
    grids.GridProperty: (
        'name',
        'value',
    ),
    shared.Standard: (
        'name',
        'version',
        'description',
    ),
    software.TimeTransformation: (
        'description',
        'mapping_type',
    ),
    shared.DocGenealogy: (
        'relationships',
    ),
    software.Deployment: (
        'executable_arguments',
        'parallelisation',
        'deployment_date',
        'executable_name',
        'platform',
        'description',
    ),
    shared.Relationship: (
        'description',
        'direction',
    ),
    shared.Machine: (
        'libraries',
        'system',
        'cores_per_processor',
        'location',
        'type',
        'name',
        'maximum_processors',
        'vendor',
        'description',
        'operating_system',
        'processor_type',
        'interconnect',
    ),
    software.ModelComponent: (
        'language',
        'dependencies',
        'citations',
        'activity',
        'purpose',
        'deployments',
        'online_resource',
        'release_date',
        'parent',
        'sub_components',
        'meta',
        'long_name',
        'grid',
        'properties',
        'type',
        'composition',
        'code_access',
        'is_embedded',
        'funding_sources',
        'license',
        'types',
        'previous_version',
        'short_name',
        'responsible_parties',
        'version',
        'coupling_framework',
        'timing',
        'description',
    ),
    activity.OutputRequirement: (
        'options',
        'id',
        'description',
        'source',
        'name',
        'requirement_type',
    ),
    grids.GridTileResolutionType: (
        'description',
        'properties',
    ),
    shared.Platform: (
        'short_name',
        'meta',
        'description',
        'long_name',
        'units',
        'contacts',
    ),
    data.DataTopic: (
        'name',
        'unit',
        'description',
    ),
    activity.MeasurementCampaign: (
        'duration',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    shared.Calendar: (
        'length',
        'range',
        'description',
    ),
    software.CouplingEndpoint: (
        'instance_id',
        'properties',
        'data_source',
    ),
    shared.DocRelationship: (
        'type',
        'direction',
        'target',
        'description',
    ),
    grids.SimpleGridGeometry: (
        'ycoords',
        'is_mesh',
        'zcoords',
        'xcoords',
        'dim_order',
        'num_dims',
    ),
    shared.DocMetaInfo: (
        'drs_path',
        'id',
        'source',
        'drs_keys',
        'source_key',
        'version',
        'status',
        'sort_key',
        'genealogy',
        'type',
        'type_display_name',
        'project',
        'author',
        'external_ids',
        'type_sort_key',
        'create_date',
        'institute',
        'update_date',
        'language',
    ),
    activity.NumericalExperiment: (
        'requirements',
        'supports',
        'meta',
        'generates',
        'description',
        'short_name',
        'funding_sources',
        'experiment_id',
        'requires',
        'measurement_campaigns',
        'long_name',
        'rationales',
        'projects',
        'responsible_parties',
    ),
    activity.PhysicalModification: (
        'type',
        'description',
        'is_conformant',
        'sources',
        'requirements',
        'frequency',
    ),
    activity.SimulationComposite: (
        'long_name',
        'child',
        'spinup_date_range',
        'date_range',
        'funding_sources',
        'control_simulation',
        'supports',
        'rank',
        'description',
        'deployments',
        'calendar',
        'inputs',
        'responsible_parties',
        'spinup_simulation',
        'outputs',
        'rationales',
        'simulation_id',
        'restarts',
        'short_name',
        'meta',
        'authors',
        'projects',
        'conformances',
    ),
    shared.License: (
        'contact',
        'description',
        'is_unrestricted',
        'name',
    ),
    shared.Compiler: (
        'options',
        'language',
        'version',
        'type',
        'name',
        'environment_variables',
    ),
    software.Rank: (
        'increment',
        'value',
        'max',
        'min',
    ),
    shared.StandardName: (
        'is_open',
        'standards',
        'value',
    ),
}

# Supported class own properties.
CLASS_OWN_PROPERTIES = { 
    shared.Property: (
        'name',
        'value',
    ),
    grids.VerticalCoordinateList: (
        'form',
        'type',
        'properties',
    ),
    software.Coupling: (
        'target',
        'priming',
        'time_lag',
        'type',
        'sources',
        'connections',
        'spatial_regriddings',
        'description',
        'properties',
        'time_transformation',
        'transformers',
        'purpose',
        'time_profile',
        'is_fully_specified',
    ),
    data.DataStorage: (
        'format',
        'size',
        'modification_date',
        'location',
    ),
    activity.InitialCondition: (
    ),
    shared.ResponsibleParty: (
        'url',
        'individual_name',
        'abbreviation',
        'organisation_name',
        'address',
        'role',
        'email',
    ),
    software.CouplingProperty: (
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    software.EntryPoint: (
        'name',
    ),
    quality.Evaluation: (
        'date',
        'type',
        'specification',
        'specification_hyperlink',
        'title',
        'did_pass',
        'type_hyperlink',
        'description',
        'explanation',
    ),
    shared.DocReference: (
        'id',
        'description',
        'changes',
        'url',
        'type',
        'name',
        'external_id',
        'version',
    ),
    software.ConnectionProperty: (
    ),
    software.ProcessorComponent: (
        'meta',
    ),
    software.ComponentLanguage: (
        'name',
        'properties',
    ),
    shared.RealCalendar: (
    ),
    data.DataRestriction: (
        'license',
        'scope',
        'restriction',
    ),
    shared.Citation: (
        'alternative_title',
        'date_type',
        'collective_title',
        'organisation',
        'location',
        'role',
        'date',
        'title',
        'type',
    ),
    data.DataHierarchyLevel: (
        'is_open',
        'value',
        'name',
    ),
    activity.LateralBoundaryCondition: (
    ),
    shared.DateRange: (
        'duration',
    ),
    shared.Daily360: (
    ),
    activity.ExperimentRelationship: (
        'target',
        'type',
    ),
    software.SpatialRegriddingUserMethod: (
        'file',
        'name',
    ),
    grids.GridMosaic: (
        'short_name',
        'id',
        'mnemonic',
        'mosaics',
        'type',
        'is_leaf',
        'description',
        'tile_count',
        'extent',
        'long_name',
        'mosaic_count',
        'tiles',
        'has_congruent_tiles',
        'citations',
    ),
    data.DataExtentTemporal: (
        'time_interval',
        'begin',
        'end',
    ),
    software.SpatialRegriddingProperty: (
    ),
    data.DataExtent: (
        'geographical',
        'temporal',
    ),
    grids.GridExtent: (
        'units',
        'minimum_longitude',
        'minimum_latitude',
        'maximum_latitude',
        'maximum_longitude',
    ),
    activity.Activity: (
        'responsible_parties',
        'funding_sources',
        'rationales',
        'projects',
    ),
    grids.GridSpec: (
        'esm_exchange_grids',
        'meta',
        'esm_model_grids',
    ),
    shared.Change: (
        'description',
        'name',
        'details',
        'author',
        'date',
        'type',
    ),
    activity.SimulationRelationshipTarget: (
        'simulation',
        'target',
    ),
    software.Component: (
        'dependencies',
        'version',
        'deployments',
        'description',
        'funding_sources',
        'grid',
        'is_embedded',
        'language',
        'license',
        'long_name',
        'online_resource',
        'parent',
        'sub_components',
        'previous_version',
        'citations',
        'properties',
        'code_access',
        'release_date',
        'composition',
        'responsible_parties',
        'coupling_framework',
        'short_name',
    ),
    software.SpatialRegridding: (
        'user_method',
        'standard_method',
        'dimension',
        'properties',
    ),
    quality.Report: (
        'evaluator',
        'date',
        'measure',
        'evaluation',
    ),
    shared.PerpetualPeriod: (
    ),
    data.DataStorageIp: (
        'protocol',
        'file_name',
        'path',
        'host',
    ),
    shared.ClosedDateRange: (
        'end',
        'start',
    ),
    activity.Conformance: (
        'description',
        'sources',
        'frequency',
        'type',
        'is_conformant',
        'requirements',
    ),
    data.DataProperty: (
        'description',
    ),
    activity.BoundaryCondition: (
    ),
    software.ConnectionEndpoint: (
        'properties',
        'data_source',
        'instance_id',
    ),
    misc.DocumentSet: (
        'data',
        'grids',
        'model',
        'meta',
        'platform',
        'ensembles',
        'simulation',
        'experiment',
    ),
    software.StatisticalModelComponent: (
        'meta',
        'types',
        'type',
        'timing',
    ),
    software.Connection: (
        'target',
        'transformers',
        'priming',
        'description',
        'time_profile',
        'properties',
        'time_transformation',
        'sources',
        'spatial_regridding',
        'type',
        'time_lag',
    ),
    activity.SpatioTemporalConstraint: (
        'date_range',
        'spatial_resolution',
    ),
    data.DataExtentGeographical: (
        'west',
        'south',
        'east',
        'north',
    ),
    grids.CoordinateList: (
        'uom',
        'has_constant_offset',
        'length',
    ),
    software.TimeLag: (
        'units',
        'value',
    ),
    shared.MachineCompilerUnit: (
        'compilers',
        'machine',
    ),
    activity.SimulationRun: (
        'model',
        'date_range',
        'meta',
    ),
    data.DataStorageDb: (
        'owner',
        'access_string',
        'table',
        'name',
    ),
    activity.Experiment: (
        'measurement_campaigns',
        'supports',
        'generates',
        'requires',
    ),
    software.ComponentLanguageProperty: (
    ),
    data.DataExtentTimeInterval: (
        'unit',
        'factor',
        'radix',
    ),
    quality.Measure: (
        'description',
        'name',
        'identification',
    ),
    activity.ExperimentRelationshipTarget: (
        'numerical_experiment',
    ),
    shared.OpenDateRange: (
        'end',
        'start',
    ),
    data.DataContent: (
        'topic',
        'aggregation',
        'frequency',
    ),
    grids.GridTile: (
        'geometry_type',
        'zcoords',
        'horizontal_resolution',
        'id',
        'area',
        'is_conformal',
        'cell_array',
        'is_regular',
        'cell_ref_array',
        'is_terrain_following',
        'coord_file',
        'is_uniform',
        'coordinate_pole',
        'long_name',
        'horizontal_crs',
        'vertical_crs',
        'mnemonic',
        'grid_north_pole',
        'nx',
        'simple_grid_geom',
        'ny',
        'nz',
        'description',
        'discretization_type',
        'short_name',
        'refinement_scheme',
        'extent',
        'vertical_resolution',
    ),
    software.Parallelisation: (
        'processes',
        'ranks',
    ),
    activity.DownscalingSimulation: (
        'downscaling_type',
        'meta',
        'outputs',
        'downscaling_id',
        'downscaled_from',
        'calendar',
        'inputs',
    ),
    activity.Ensemble: (
        'outputs',
        'members',
        'types',
        'meta',
    ),
    shared.ChangeProperty: (
        'description',
        'id',
    ),
    data.DataObject: (
        'distribution',
        'geometry_model',
        'purpose',
        'content',
        'source_simulation',
        'keyword',
        'data_status',
        'acronym',
        'meta',
        'extent',
        'properties',
        'description',
        'hierarchy_level',
        'storage',
        'restriction',
        'parent_object',
        'citations',
        'child_object',
    ),
    data.DataStorageFile: (
        'file_name',
        'path',
        'file_system',
    ),
    activity.EnsembleMember: (
        'simulation',
        'ensemble',
        'ensemble_ids',
    ),
    activity.SimulationRelationship: (
        'target',
        'type',
    ),
    data.DataDistribution: (
        'responsible_party',
        'format',
        'access',
        'fee',
    ),
    shared.DocRelationshipTarget: (
        'reference',
    ),
    software.ComponentProperty: (
        'values',
        'grid',
        'sub_properties',
        'standard_names',
        'intent',
        'description',
        'units',
        'citations',
        'short_name',
        'long_name',
        'is_represented',
    ),
    activity.Simulation: (
        'restarts',
        'inputs',
        'spinup_date_range',
        'control_simulation',
        'authors',
        'spinup_simulation',
        'simulation_id',
        'outputs',
        'conformances',
        'deployments',
        'calendar',
    ),
    software.Timing: (
        'start',
        'units',
        'end',
        'rate',
        'is_variable_rate',
    ),
    quality.CimQuality: (
        'meta',
        'reports',
    ),
    activity.NumericalRequirement: (
        'options',
        'id',
        'description',
        'source',
        'requirement_type',
        'name',
    ),
    activity.NumericalRequirementOption: (
        'sub_options',
        'name',
        'relationship',
        'description',
        'id',
    ),
    activity.NumericalActivity: (
        'supports',
        'description',
        'short_name',
        'long_name',
    ),
    shared.DataSource: (
        'purpose',
    ),
    grids.GridProperty: (
    ),
    shared.Standard: (
        'version',
        'description',
        'name',
    ),
    software.TimeTransformation: (
        'description',
        'mapping_type',
    ),
    shared.DocGenealogy: (
        'relationships',
    ),
    software.Deployment: (
        'parallelisation',
        'platform',
        'description',
        'executable_name',
        'executable_arguments',
        'deployment_date',
    ),
    shared.Relationship: (
        'description',
        'direction',
    ),
    shared.Machine: (
        'libraries',
        'system',
        'cores_per_processor',
        'location',
        'type',
        'operating_system',
        'maximum_processors',
        'vendor',
        'description',
        'name',
        'processor_type',
        'interconnect',
    ),
    software.ModelComponent: (
        'activity',
        'type',
        'meta',
        'types',
        'timing',
    ),
    activity.OutputRequirement: (
    ),
    grids.GridTileResolutionType: (
        'description',
        'properties',
    ),
    shared.Platform: (
        'meta',
        'units',
        'contacts',
        'description',
        'long_name',
        'short_name',
    ),
    data.DataTopic: (
        'unit',
        'description',
        'name',
    ),
    activity.MeasurementCampaign: (
        'duration',
    ),
    shared.Calendar: (
        'range',
        'description',
        'length',
    ),
    software.CouplingEndpoint: (
        'properties',
        'data_source',
        'instance_id',
    ),
    shared.DocRelationship: (
        'type',
        'target',
    ),
    grids.SimpleGridGeometry: (
        'xcoords',
        'dim_order',
        'ycoords',
        'is_mesh',
        'zcoords',
        'num_dims',
    ),
    shared.DocMetaInfo: (
        'status',
        'type_sort_key',
        'drs_path',
        'source',
        'type_display_name',
        'language',
        'drs_keys',
        'institute',
        'source_key',
        'author',
        'update_date',
        'external_ids',
        'sort_key',
        'type',
        'version',
        'create_date',
        'project',
        'genealogy',
        'id',
    ),
    activity.NumericalExperiment: (
        'requirements',
        'meta',
        'description',
        'short_name',
        'experiment_id',
        'long_name',
    ),
    activity.PhysicalModification: (
    ),
    activity.SimulationComposite: (
        'meta',
        'rank',
        'child',
        'date_range',
    ),
    shared.License: (
        'contact',
        'name',
        'is_unrestricted',
        'description',
    ),
    shared.Compiler: (
        'language',
        'version',
        'name',
        'environment_variables',
        'options',
        'type',
    ),
    software.Rank: (
        'increment',
        'min',
        'value',
        'max',
    ),
    shared.StandardName: (
        'is_open',
        'value',
        'standards',
    ),
}

# Total class properties.
TOTAL_CLASS_PROPERTIES = sum(len(i) for i in CLASS_OWN_PROPERTIES.values())

# ------------------------------------------------
# Enum.
# ------------------------------------------------

# Supported enums.
ENUMS = (
    shared.MachineType,
    software.ComponentPropertyIntentType,
    quality.CimResultType,
    grids.FeatureTypeEnum,
    activity.FrequencyType,
    activity.ProjectType,
    shared.InterconnectType,
    software.ConnectionType,
    shared.ChangePropertyType,
    grids.GridTypeEnum,
    activity.SimulationType,
    grids.VerticalCsEnum,
    shared.DocRelationshipDirectionType,
    software.ModelComponentType,
    shared.OperatingSystemType,
    software.SpatialRegriddingDimensionType,
    software.CouplingFrameworkType,
    activity.DownscalingType,
    shared.DocRelationshipType,
    quality.QualityStatusType,
    shared.DataPurpose,
    activity.ConformanceType,
    software.SpatialRegriddingStandardMethodType,
    grids.DiscretizationEnum,
    shared.ProcessorType,
    activity.SimulationRelationshipType,
    data.DataHierarchyType,
    data.DataStatusType,
    quality.CimFeatureType,
    grids.ArcTypeEnum,
    shared.UnitType,
    shared.MachineVendorType,
    shared.CompilerType,
    quality.CimScopeCodeType,
    software.StatisticalModelComponentType,
    grids.GeometryTypeEnum,
    software.TimeMappingType,
    software.TimingUnits,
    grids.HorizontalCsEnum,
    activity.EnsembleType,
    grids.RefinementTypeEnum,
    activity.ExperimentRelationshipType,
    quality.QualitySeverityType,
    shared.DocStatusType,
    grids.GridNodePositionEnum,
    shared.DocType,
    quality.QualityIssueType,
    activity.ResolutionType,
)

# Total enum members across all enums.
TOTAL_ENUM_MEMBERS = sum(len(e.members) for e in ENUMS)


# ------------------------------------------------
# Type hierarchies.
# ------------------------------------------------

# Set of supported types.
TYPES = CLASSES + ENUMS

# Supported document types.
DOCUMENT_TYPES = (
    shared.Platform,
    data.DataObject,
    grids.GridSpec,
    quality.CimQuality,
    misc.DocumentSet,
    activity.SimulationComposite,
    activity.Ensemble,
    activity.NumericalExperiment,
    activity.SimulationRun,
    activity.DownscalingSimulation,
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
)

# Base classes.
BASE_CLASSES = defaultdict(tuple)
BASE_CLASSES[grids.VerticalCoordinateList] = (grids.CoordinateList, )
BASE_CLASSES[activity.InitialCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[software.CouplingProperty] = (shared.Property, )
BASE_CLASSES[software.ConnectionProperty] = (shared.Property, )
BASE_CLASSES[software.ProcessorComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[shared.RealCalendar] = (shared.Calendar, )
BASE_CLASSES[activity.LateralBoundaryCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[shared.Daily360] = (shared.Calendar, )
BASE_CLASSES[activity.ExperimentRelationship] = (shared.Relationship, )
BASE_CLASSES[software.SpatialRegriddingProperty] = (shared.Property, )
BASE_CLASSES[software.Component] = (shared.DataSource, )
BASE_CLASSES[shared.PerpetualPeriod] = (shared.Calendar, )
BASE_CLASSES[data.DataStorageIp] = (data.DataStorage, )
BASE_CLASSES[shared.ClosedDateRange] = (shared.DateRange, )
BASE_CLASSES[data.DataProperty] = (shared.Property, )
BASE_CLASSES[activity.BoundaryCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[software.StatisticalModelComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[activity.SpatioTemporalConstraint] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.SimulationRun] = (activity.Simulation, activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[data.DataStorageDb] = (data.DataStorage, )
BASE_CLASSES[activity.Experiment] = (activity.Activity, )
BASE_CLASSES[software.ComponentLanguageProperty] = (shared.Property, )
BASE_CLASSES[shared.OpenDateRange] = (shared.DateRange, )
BASE_CLASSES[data.DataContent] = (shared.DataSource, )
BASE_CLASSES[activity.DownscalingSimulation] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.Ensemble] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[shared.ChangeProperty] = (shared.Property, )
BASE_CLASSES[data.DataObject] = (shared.DataSource, )
BASE_CLASSES[data.DataStorageFile] = (data.DataStorage, )
BASE_CLASSES[activity.EnsembleMember] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.SimulationRelationship] = (shared.Relationship, )
BASE_CLASSES[software.ComponentProperty] = (shared.DataSource, )
BASE_CLASSES[activity.Simulation] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.NumericalActivity] = (activity.Activity, )
BASE_CLASSES[grids.GridProperty] = (shared.Property, )
BASE_CLASSES[software.ModelComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[activity.OutputRequirement] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.MeasurementCampaign] = (activity.Activity, )
BASE_CLASSES[shared.DocRelationship] = (shared.Relationship, )
BASE_CLASSES[activity.NumericalExperiment] = (activity.Experiment, activity.Activity, )
BASE_CLASSES[activity.PhysicalModification] = (activity.Conformance, )
BASE_CLASSES[activity.SimulationComposite] = (activity.Simulation, activity.NumericalActivity, activity.Activity, )

# Classes with base classes.
BASE_CLASSED = tuple(BASE_CLASSES.keys())

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
SUB_CLASSES[activity.Conformance] = (
    activity.PhysicalModification,
    )
SUB_CLASSES[shared.DataSource] = (
    data.DataContent,
    data.DataObject,
    software.Component,
    software.ComponentProperty,
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
    )
SUB_CLASSES[shared.Calendar] = (
    shared.PerpetualPeriod,
    shared.RealCalendar,
    shared.Daily360,
    )
SUB_CLASSES[grids.CoordinateList] = (
    grids.VerticalCoordinateList,
    )
SUB_CLASSES[shared.DateRange] = (
    shared.ClosedDateRange,
    shared.OpenDateRange,
    )
SUB_CLASSES[data.DataStorage] = (
    data.DataStorageIp,
    data.DataStorageDb,
    data.DataStorageFile,
    )
SUB_CLASSES[shared.Property] = (
    data.DataProperty,
    software.ConnectionProperty,
    software.ComponentLanguageProperty,
    software.SpatialRegriddingProperty,
    software.CouplingProperty,
    grids.GridProperty,
    shared.ChangeProperty,
    )
SUB_CLASSES[software.Component] = (
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
    )
SUB_CLASSES[activity.Activity] = (
    activity.MeasurementCampaign,
    activity.NumericalActivity,
    activity.Experiment,
    activity.Ensemble,
    activity.Simulation,
    activity.NumericalExperiment,
    activity.EnsembleMember,
    activity.DownscalingSimulation,
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[activity.Experiment] = (
    activity.NumericalExperiment,
    )
SUB_CLASSES[activity.Simulation] = (
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[shared.Relationship] = (
    activity.SimulationRelationship,
    activity.ExperimentRelationship,
    shared.DocRelationship,
    )
SUB_CLASSES[activity.NumericalActivity] = (
    activity.Ensemble,
    activity.Simulation,
    activity.EnsembleMember,
    activity.DownscalingSimulation,
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[activity.NumericalRequirement] = (
    activity.OutputRequirement,
    activity.BoundaryCondition,
    activity.InitialCondition,
    activity.LateralBoundaryCondition,
    activity.SpatioTemporalConstraint,
    )

# Classes that have been sub classed.
SUB_CLASSED = tuple(SUB_CLASSES.keys())

# Maximum class depth in hierarchy.
CLASS_HIERACHY_DEPTH = max(len(v) for v in BASE_CLASSES.values())

# ------------------------------------------------
# Type constraints.
# ------------------------------------------------

# Map of ontology types to constraints.
CONSTRAINTS = {
    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    shared.Property: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    grids.VerticalCoordinateList: (

        ('has_constant_offset', 'type', bool),
        ('form', 'type', unicode),
        ('length', 'type', int),
        ('type', 'type', unicode),
        ('properties', 'type', grids.GridProperty),
        ('uom', 'type', unicode),

        ('has_constant_offset', 'cardinality', "0.1"),
        ('form', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('uom', 'cardinality', "0.1"),

    ),
    software.Coupling: (

        ('transformers', 'type', software.ProcessorComponent),
        ('target', 'type', software.CouplingEndpoint),
        ('type', 'type', unicode),
        ('time_transformation', 'type', software.TimeTransformation),
        ('connections', 'type', software.Connection),
        ('sources', 'type', software.CouplingEndpoint),
        ('spatial_regriddings', 'type', software.SpatialRegridding),
        ('purpose', 'type', unicode),
        ('time_profile', 'type', software.Timing),
        ('priming', 'type', shared.DataSource),
        ('is_fully_specified', 'type', bool),
        ('properties', 'type', software.CouplingProperty),
        ('time_lag', 'type', software.TimeLag),
        ('description', 'type', unicode),

        ('transformers', 'cardinality', "0.N"),
        ('target', 'cardinality', "1.1"),
        ('type', 'cardinality', "0.1"),
        ('time_transformation', 'cardinality', "0.1"),
        ('connections', 'cardinality', "0.N"),
        ('sources', 'cardinality', "1.N"),
        ('spatial_regriddings', 'cardinality', "0.N"),
        ('purpose', 'cardinality', "1.1"),
        ('time_profile', 'cardinality', "0.1"),
        ('priming', 'cardinality', "0.1"),
        ('is_fully_specified', 'cardinality', "1.1"),
        ('properties', 'cardinality', "0.N"),
        ('time_lag', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    data.DataStorage: (

        ('size', 'type', int),
        ('location', 'type', unicode),
        ('modification_date', 'type', datetime.datetime),
        ('format', 'type', unicode),

        ('size', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('modification_date', 'cardinality', "0.1"),
        ('format', 'cardinality', "0.1"),

    ),
    activity.InitialCondition: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "initialCondition"),
    ),
    shared.ResponsibleParty: (

        ('url', 'type', unicode),
        ('email', 'type', unicode),
        ('abbreviation', 'type', unicode),
        ('individual_name', 'type', unicode),
        ('role', 'type', unicode),
        ('address', 'type', unicode),
        ('organisation_name', 'type', unicode),

        ('url', 'cardinality', "0.1"),
        ('email', 'cardinality', "0.1"),
        ('abbreviation', 'cardinality', "0.1"),
        ('individual_name', 'cardinality', "0.1"),
        ('role', 'cardinality', "0.1"),
        ('address', 'cardinality', "0.1"),
        ('organisation_name', 'cardinality', "0.1"),

    ),
    software.CouplingProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    software.Composition: (

        ('couplings', 'type', unicode),
        ('description', 'type', unicode),

        ('couplings', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),

    ),
    software.EntryPoint: (

        ('name', 'type', unicode),

        ('name', 'cardinality', "0.1"),

    ),
    quality.Evaluation: (

        ('description', 'type', unicode),
        ('title', 'type', unicode),
        ('specification', 'type', unicode),
        ('specification_hyperlink', 'type', unicode),
        ('did_pass', 'type', bool),
        ('type_hyperlink', 'type', unicode),
        ('date', 'type', datetime.datetime),
        ('type', 'type', unicode),
        ('explanation', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('title', 'cardinality', "0.1"),
        ('specification', 'cardinality', "0.1"),
        ('specification_hyperlink', 'cardinality', "0.1"),
        ('did_pass', 'cardinality', "0.1"),
        ('type_hyperlink', 'cardinality', "0.1"),
        ('date', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('explanation', 'cardinality', "0.1"),

    ),
    shared.DocReference: (

        ('name', 'type', unicode),
        ('url', 'type', unicode),
        ('changes', 'type', shared.Change),
        ('version', 'type', int),
        ('type', 'type', unicode),
        ('external_id', 'type', unicode),
        ('id', 'type', uuid.UUID),
        ('description', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('url', 'cardinality', "0.1"),
        ('changes', 'cardinality', "0.N"),
        ('version', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('external_id', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    software.ConnectionProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    software.ProcessorComponent: (

        ('funding_sources', 'type', unicode),
        ('version', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('is_embedded', 'type', bool),
        ('short_name', 'type', unicode),
        ('previous_version', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('citations', 'type', shared.Citation),
        ('composition', 'type', software.Composition),
        ('coupling_framework', 'type', unicode),
        ('description', 'type', unicode),
        ('parent', 'type', software.Component),
        ('sub_components', 'type', software.Component),
        ('dependencies', 'type', software.EntryPoint),
        ('grid', 'type', grids.GridSpec),
        ('purpose', 'type', unicode),
        ('online_resource', 'type', unicode),
        ('properties', 'type', software.ComponentProperty),
        ('language', 'type', software.ComponentLanguage),
        ('license', 'type', shared.License),
        ('release_date', 'type', datetime.datetime),
        ('code_access', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('version', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('is_embedded', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('previous_version', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('citations', 'cardinality', "0.N"),
        ('composition', 'cardinality', "0.1"),
        ('coupling_framework', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('parent', 'cardinality', "0.1"),
        ('sub_components', 'cardinality', "0.N"),
        ('dependencies', 'cardinality', "0.N"),
        ('grid', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('online_resource', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('language', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('code_access', 'cardinality', "0.1"),

    ),
    software.ComponentLanguage: (

        ('name', 'type', unicode),
        ('properties', 'type', software.ComponentLanguageProperty),

        ('name', 'cardinality', "1.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    shared.RealCalendar: (

        ('length', 'type', int),
        ('range', 'type', shared.DateRange),
        ('description', 'type', unicode),

        ('length', 'cardinality', "0.1"),
        ('range', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    data.DataRestriction: (

        ('restriction', 'type', unicode),
        ('license', 'type', shared.License),
        ('scope', 'type', unicode),

        ('restriction', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('scope', 'cardinality', "0.1"),

    ),
    shared.Citation: (

        ('alternative_title', 'type', unicode),
        ('date_type', 'type', unicode),
        ('collective_title', 'type', unicode),
        ('role', 'type', unicode),
        ('location', 'type', unicode),
        ('date', 'type', datetime.datetime),
        ('title', 'type', unicode),
        ('type', 'type', unicode),
        ('organisation', 'type', unicode),

        ('alternative_title', 'cardinality', "0.1"),
        ('date_type', 'cardinality', "0.1"),
        ('collective_title', 'cardinality', "0.1"),
        ('role', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('date', 'cardinality', "0.1"),
        ('title', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('organisation', 'cardinality', "0.1"),

    ),
    data.DataHierarchyLevel: (

        ('is_open', 'type', bool),
        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('is_open', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    activity.LateralBoundaryCondition: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "lateralBoundaryCondition"),
    ),
    shared.DateRange: (

        ('duration', 'type', unicode),

        ('duration', 'cardinality', "0.1"),

    ),
    shared.Daily360: (

        ('length', 'type', int),
        ('range', 'type', shared.DateRange),
        ('description', 'type', unicode),

        ('length', 'cardinality', "0.1"),
        ('range', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    activity.ExperimentRelationship: (

        ('direction', 'type', unicode),
        ('type', 'type', unicode),
        ('description', 'type', unicode),
        ('target', 'type', activity.ExperimentRelationshipTarget),

        ('direction', 'cardinality', "1.1"),
        ('type', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('target', 'cardinality', "1.1"),

    ),
    software.SpatialRegriddingUserMethod: (

        ('name', 'type', unicode),
        ('file', 'type', data.DataObject),

        ('name', 'cardinality', "1.1"),
        ('file', 'cardinality', "0.1"),

    ),
    grids.GridMosaic: (

        ('is_leaf', 'type', bool),
        ('mosaic_count', 'type', int),
        ('tiles', 'type', grids.GridTile),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('type', 'type', unicode),
        ('long_name', 'type', unicode),
        ('tile_count', 'type', int),
        ('citations', 'type', shared.Citation),
        ('extent', 'type', grids.GridExtent),
        ('mnemonic', 'type', unicode),
        ('has_congruent_tiles', 'type', bool),
        ('mosaics', 'type', grids.GridMosaic),
        ('id', 'type', unicode),

        ('is_leaf', 'cardinality', "1.1"),
        ('mosaic_count', 'cardinality', "0.1"),
        ('tiles', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('type', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('tile_count', 'cardinality', "0.1"),
        ('citations', 'cardinality', "0.N"),
        ('extent', 'cardinality', "0.1"),
        ('mnemonic', 'cardinality', "0.1"),
        ('has_congruent_tiles', 'cardinality', "0.1"),
        ('mosaics', 'cardinality', "0.N"),
        ('id', 'cardinality', "1.1"),

    ),
    data.DataExtentTemporal: (

        ('time_interval', 'type', data.DataExtentTimeInterval),
        ('begin', 'type', datetime.date),
        ('end', 'type', datetime.date),

        ('time_interval', 'cardinality', "0.1"),
        ('begin', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),

    ),
    software.SpatialRegriddingProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    data.DataExtent: (

        ('temporal', 'type', data.DataExtentTemporal),
        ('geographical', 'type', data.DataExtentGeographical),

        ('temporal', 'cardinality', "1.1"),
        ('geographical', 'cardinality', "1.1"),

    ),
    grids.GridExtent: (

        ('units', 'type', unicode),
        ('maximum_latitude', 'type', unicode),
        ('minimum_latitude', 'type', unicode),
        ('maximum_longitude', 'type', unicode),
        ('minimum_longitude', 'type', unicode),

        ('units', 'cardinality', "0.1"),
        ('maximum_latitude', 'cardinality', "1.1"),
        ('minimum_latitude', 'cardinality', "1.1"),
        ('maximum_longitude', 'cardinality', "1.1"),
        ('minimum_longitude', 'cardinality', "1.1"),

    ),
    activity.Activity: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('projects', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    grids.GridSpec: (

        ('esm_exchange_grids', 'type', grids.GridMosaic),
        ('meta', 'type', shared.DocMetaInfo),
        ('esm_model_grids', 'type', grids.GridMosaic),

        ('esm_exchange_grids', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('esm_model_grids', 'cardinality', "0.N"),

    ),
    shared.Change: (

        ('description', 'type', unicode),
        ('author', 'type', shared.ResponsibleParty),
        ('details', 'type', shared.ChangeProperty),
        ('date', 'type', datetime.datetime),
        ('type', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('author', 'cardinality', "0.1"),
        ('details', 'cardinality', "1.N"),
        ('date', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

    ),
    activity.SimulationRelationshipTarget: (

        ('target', 'type', unicode),
        ('simulation', 'type', shared.DocReference),

        ('target', 'cardinality', "0.1"),
        ('simulation', 'cardinality', "0.1"),

    ),
    software.Component: (

        ('funding_sources', 'type', unicode),
        ('version', 'type', unicode),
        ('long_name', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('short_name', 'type', unicode),
        ('previous_version', 'type', unicode),
        ('is_embedded', 'type', bool),
        ('deployments', 'type', software.Deployment),
        ('citations', 'type', shared.Citation),
        ('composition', 'type', software.Composition),
        ('coupling_framework', 'type', unicode),
        ('description', 'type', unicode),
        ('parent', 'type', software.Component),
        ('sub_components', 'type', software.Component),
        ('dependencies', 'type', software.EntryPoint),
        ('grid', 'type', grids.GridSpec),
        ('purpose', 'type', unicode),
        ('online_resource', 'type', unicode),
        ('properties', 'type', software.ComponentProperty),
        ('language', 'type', software.ComponentLanguage),
        ('license', 'type', shared.License),
        ('release_date', 'type', datetime.datetime),
        ('code_access', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('version', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('short_name', 'cardinality', "1.1"),
        ('previous_version', 'cardinality', "0.1"),
        ('is_embedded', 'cardinality', "0.1"),
        ('deployments', 'cardinality', "0.N"),
        ('citations', 'cardinality', "0.N"),
        ('composition', 'cardinality', "0.1"),
        ('coupling_framework', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('parent', 'cardinality', "0.1"),
        ('sub_components', 'cardinality', "0.N"),
        ('dependencies', 'cardinality', "0.N"),
        ('grid', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('online_resource', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('language', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('code_access', 'cardinality', "0.1"),

    ),
    software.SpatialRegridding: (

        ('user_method', 'type', software.SpatialRegriddingUserMethod),
        ('properties', 'type', software.SpatialRegriddingProperty),
        ('standard_method', 'type', unicode),
        ('dimension', 'type', unicode),

        ('user_method', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('standard_method', 'cardinality', "0.1"),
        ('dimension', 'cardinality', "0.1"),

    ),
    quality.Report: (

        ('date', 'type', datetime.datetime),
        ('evaluator', 'type', shared.ResponsibleParty),
        ('evaluation', 'type', quality.Evaluation),
        ('measure', 'type', quality.Measure),

        ('date', 'cardinality', "0.1"),
        ('evaluator', 'cardinality', "0.1"),
        ('evaluation', 'cardinality', "1.1"),
        ('measure', 'cardinality', "1.1"),

    ),
    shared.PerpetualPeriod: (

        ('length', 'type', int),
        ('range', 'type', shared.DateRange),
        ('description', 'type', unicode),

        ('length', 'cardinality', "0.1"),
        ('range', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    data.DataStorageIp: (

        ('protocol', 'type', unicode),
        ('modification_date', 'type', datetime.datetime),
        ('format', 'type', unicode),
        ('file_name', 'type', unicode),
        ('host', 'type', unicode),
        ('location', 'type', unicode),
        ('path', 'type', unicode),
        ('size', 'type', int),

        ('protocol', 'cardinality', "0.1"),
        ('modification_date', 'cardinality', "0.1"),
        ('format', 'cardinality', "0.1"),
        ('file_name', 'cardinality', "0.1"),
        ('host', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('path', 'cardinality', "0.1"),
        ('size', 'cardinality', "0.1"),

    ),
    shared.ClosedDateRange: (

        ('duration', 'type', unicode),
        ('start', 'type', datetime.datetime),
        ('end', 'type', datetime.datetime),

        ('duration', 'cardinality', "0.1"),
        ('start', 'cardinality', "1.1"),
        ('end', 'cardinality', "0.1"),

    ),
    activity.Conformance: (

        ('requirements', 'type', activity.NumericalRequirement),
        ('description', 'type', unicode),
        ('sources', 'type', shared.DataSource),
        ('frequency', 'type', unicode),
        ('is_conformant', 'type', bool),
        ('type', 'type', unicode),

        ('requirements', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('sources', 'cardinality', "0.N"),
        ('frequency', 'cardinality', "0.1"),
        ('is_conformant', 'cardinality', "1.1"),
        ('type', 'cardinality', "0.1"),

    ),
    data.DataProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),
        ('description', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    activity.BoundaryCondition: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "boundaryCondition"),
    ),
    software.ConnectionEndpoint: (

        ('instance_id', 'type', unicode),
        ('data_source', 'type', shared.DataSource),
        ('properties', 'type', software.ConnectionProperty),

        ('instance_id', 'cardinality', "0.1"),
        ('data_source', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    misc.DocumentSet: (

        ('ensembles', 'type', activity.Ensemble),
        ('grids', 'type', grids.GridSpec),
        ('experiment', 'type', activity.NumericalExperiment),
        ('simulation', 'type', activity.SimulationRun),
        ('platform', 'type', shared.Platform),
        ('meta', 'type', shared.DocMetaInfo),
        ('model', 'type', software.ModelComponent),
        ('data', 'type', data.DataObject),

        ('ensembles', 'cardinality', "0.N"),
        ('grids', 'cardinality', "0.N"),
        ('experiment', 'cardinality', "0.1"),
        ('simulation', 'cardinality', "0.1"),
        ('platform', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('model', 'cardinality', "0.1"),
        ('data', 'cardinality', "0.N"),

    ),
    software.StatisticalModelComponent: (

        ('funding_sources', 'type', unicode),
        ('version', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('is_embedded', 'type', bool),
        ('short_name', 'type', unicode),
        ('previous_version', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('citations', 'type', shared.Citation),
        ('type', 'type', unicode),
        ('composition', 'type', software.Composition),
        ('coupling_framework', 'type', unicode),
        ('description', 'type', unicode),
        ('parent', 'type', software.Component),
        ('sub_components', 'type', software.Component),
        ('dependencies', 'type', software.EntryPoint),
        ('grid', 'type', grids.GridSpec),
        ('purpose', 'type', unicode),
        ('online_resource', 'type', unicode),
        ('timing', 'type', software.Timing),
        ('properties', 'type', software.ComponentProperty),
        ('types', 'type', unicode),
        ('language', 'type', software.ComponentLanguage),
        ('license', 'type', shared.License),
        ('release_date', 'type', datetime.datetime),
        ('code_access', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('version', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('is_embedded', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('previous_version', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('citations', 'cardinality', "0.N"),
        ('type', 'cardinality', "0.1"),
        ('composition', 'cardinality', "0.1"),
        ('coupling_framework', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('parent', 'cardinality', "0.1"),
        ('sub_components', 'cardinality', "0.N"),
        ('dependencies', 'cardinality', "0.N"),
        ('grid', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('online_resource', 'cardinality', "0.1"),
        ('timing', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('types', 'cardinality', "1.N"),
        ('language', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('code_access', 'cardinality', "0.1"),

    ),
    software.Connection: (

        ('transformers', 'type', software.ProcessorComponent),
        ('description', 'type', unicode),
        ('time_transformation', 'type', software.TimeTransformation),
        ('spatial_regridding', 'type', software.SpatialRegridding),
        ('sources', 'type', software.ConnectionEndpoint),
        ('target', 'type', software.ConnectionEndpoint),
        ('time_profile', 'type', software.Timing),
        ('type', 'type', unicode),
        ('properties', 'type', software.ConnectionProperty),
        ('time_lag', 'type', unicode),
        ('priming', 'type', shared.DataSource),

        ('transformers', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('time_transformation', 'cardinality', "0.1"),
        ('spatial_regridding', 'cardinality', "0.N"),
        ('sources', 'cardinality', "0.N"),
        ('target', 'cardinality', "0.1"),
        ('time_profile', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('time_lag', 'cardinality', "0.1"),
        ('priming', 'cardinality', "0.1"),

    ),
    activity.SpatioTemporalConstraint: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('date_range', 'type', shared.DateRange),
        ('source', 'type', shared.DataSource),
        ('spatial_resolution', 'type', unicode),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('date_range', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('spatial_resolution', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "spatioTemporalConstraint"),
    ),
    data.DataExtentGeographical: (

        ('west', 'type', float),
        ('east', 'type', float),
        ('north', 'type', float),
        ('south', 'type', float),

        ('west', 'cardinality', "0.1"),
        ('east', 'cardinality', "0.1"),
        ('north', 'cardinality', "0.1"),
        ('south', 'cardinality', "0.1"),

    ),
    grids.CoordinateList: (

        ('has_constant_offset', 'type', bool),
        ('length', 'type', int),
        ('uom', 'type', unicode),

        ('has_constant_offset', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('uom', 'cardinality', "0.1"),

    ),
    software.TimeLag: (

        ('units', 'type', unicode),
        ('value', 'type', int),

        ('units', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    shared.MachineCompilerUnit: (

        ('machine', 'type', shared.Machine),
        ('compilers', 'type', shared.Compiler),

        ('machine', 'cardinality', "1.1"),
        ('compilers', 'cardinality', "0.N"),

    ),
    activity.SimulationRun: (

        ('funding_sources', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('conformances', 'type', activity.Conformance),
        ('calendar', 'type', shared.Calendar),
        ('rationales', 'type', unicode),
        ('control_simulation', 'type', activity.Simulation),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('restarts', 'type', data.DataObject),
        ('supports', 'type', activity.Experiment),
        ('inputs', 'type', software.Coupling),
        ('simulation_id', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('outputs', 'type', data.DataObject),
        ('spinup_date_range', 'type', shared.ClosedDateRange),
        ('date_range', 'type', shared.DateRange),
        ('authors', 'type', unicode),
        ('projects', 'type', unicode),
        ('spinup_simulation', 'type', activity.Simulation),
        ('model', 'type', software.ModelComponent),

        ('funding_sources', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('conformances', 'cardinality', "0.N"),
        ('calendar', 'cardinality', "1.1"),
        ('rationales', 'cardinality', "0.N"),
        ('control_simulation', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('restarts', 'cardinality', "0.N"),
        ('supports', 'cardinality', "0.N"),
        ('inputs', 'cardinality', "0.N"),
        ('simulation_id', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('outputs', 'cardinality', "0.N"),
        ('spinup_date_range', 'cardinality', "0.1"),
        ('date_range', 'cardinality', "1.1"),
        ('authors', 'cardinality', "0.1"),
        ('projects', 'cardinality', "0.N"),
        ('spinup_simulation', 'cardinality', "0.1"),
        ('model', 'cardinality', "0.1"),

    ),
    data.DataStorageDb: (

        ('name', 'type', unicode),
        ('modification_date', 'type', datetime.datetime),
        ('format', 'type', unicode),
        ('location', 'type', unicode),
        ('owner', 'type', unicode),
        ('table', 'type', unicode),
        ('access_string', 'type', unicode),
        ('size', 'type', int),

        ('name', 'cardinality', "0.1"),
        ('modification_date', 'cardinality', "0.1"),
        ('format', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('owner', 'cardinality', "0.1"),
        ('table', 'cardinality', "0.1"),
        ('access_string', 'cardinality', "0.1"),
        ('size', 'cardinality', "0.1"),

    ),
    activity.Experiment: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('generates', 'type', unicode),
        ('requires', 'type', activity.NumericalActivity),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('measurement_campaigns', 'type', activity.MeasurementCampaign),
        ('supports', 'type', unicode),
        ('projects', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('generates', 'cardinality', "0.N"),
        ('requires', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('measurement_campaigns', 'cardinality', "0.N"),
        ('supports', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    software.ComponentLanguageProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    data.DataExtentTimeInterval: (

        ('radix', 'type', int),
        ('unit', 'type', unicode),
        ('factor', 'type', int),

        ('radix', 'cardinality', "0.1"),
        ('unit', 'cardinality', "0.1"),
        ('factor', 'cardinality', "0.1"),

    ),
    quality.Measure: (

        ('identification', 'type', unicode),
        ('description', 'type', unicode),
        ('name', 'type', unicode),

        ('identification', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

    ),
    activity.ExperimentRelationshipTarget: (

        ('numerical_experiment', 'type', activity.NumericalExperiment),

        ('numerical_experiment', 'cardinality', "0.1"),

    ),
    shared.OpenDateRange: (

        ('duration', 'type', unicode),
        ('start', 'type', datetime.datetime),
        ('end', 'type', datetime.datetime),

        ('duration', 'cardinality', "0.1"),
        ('start', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),

    ),
    data.DataContent: (

        ('topic', 'type', data.DataTopic),
        ('frequency', 'type', unicode),
        ('purpose', 'type', unicode),
        ('aggregation', 'type', unicode),

        ('topic', 'cardinality', "1.1"),
        ('frequency', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('aggregation', 'cardinality', "0.1"),

    ),
    grids.GridTile: (

        ('mnemonic', 'type', unicode),
        ('refinement_scheme', 'type', unicode),
        ('is_regular', 'type', bool),
        ('long_name', 'type', unicode),
        ('horizontal_crs', 'type', unicode),
        ('cell_array', 'type', unicode),
        ('id', 'type', unicode),
        ('cell_ref_array', 'type', unicode),
        ('area', 'type', unicode),
        ('simple_grid_geom', 'type', grids.SimpleGridGeometry),
        ('grid_north_pole', 'type', unicode),
        ('vertical_crs', 'type', unicode),
        ('nx', 'type', int),
        ('ny', 'type', int),
        ('nz', 'type', int),
        ('vertical_resolution', 'type', grids.GridTileResolutionType),
        ('discretization_type', 'type', unicode),
        ('coordinate_pole', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('extent', 'type', grids.GridExtent),
        ('zcoords', 'type', grids.VerticalCoordinateList),
        ('is_conformal', 'type', bool),
        ('is_uniform', 'type', bool),
        ('coord_file', 'type', unicode),
        ('geometry_type', 'type', unicode),
        ('horizontal_resolution', 'type', grids.GridTileResolutionType),
        ('is_terrain_following', 'type', bool),

        ('mnemonic', 'cardinality', "0.1"),
        ('refinement_scheme', 'cardinality', "0.1"),
        ('is_regular', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('horizontal_crs', 'cardinality', "0.1"),
        ('cell_array', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('cell_ref_array', 'cardinality', "0.1"),
        ('area', 'cardinality', "0.1"),
        ('simple_grid_geom', 'cardinality', "0.1"),
        ('grid_north_pole', 'cardinality', "0.1"),
        ('vertical_crs', 'cardinality', "0.1"),
        ('nx', 'cardinality', "0.1"),
        ('ny', 'cardinality', "0.1"),
        ('nz', 'cardinality', "0.1"),
        ('vertical_resolution', 'cardinality', "0.1"),
        ('discretization_type', 'cardinality', "0.1"),
        ('coordinate_pole', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "0.1"),
        ('extent', 'cardinality', "0.1"),
        ('zcoords', 'cardinality', "0.1"),
        ('is_conformal', 'cardinality', "0.1"),
        ('is_uniform', 'cardinality', "0.1"),
        ('coord_file', 'cardinality', "0.1"),
        ('geometry_type', 'cardinality', "0.1"),
        ('horizontal_resolution', 'cardinality', "0.1"),
        ('is_terrain_following', 'cardinality', "0.1"),

    ),
    software.Parallelisation: (

        ('ranks', 'type', software.Rank),
        ('processes', 'type', int),

        ('ranks', 'cardinality', "0.N"),
        ('processes', 'cardinality', "1.1"),

    ),
    activity.DownscalingSimulation: (

        ('inputs', 'type', software.Coupling),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('outputs', 'type', data.DataObject),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('long_name', 'type', unicode),
        ('downscaled_from', 'type', shared.DataSource),
        ('meta', 'type', shared.DocMetaInfo),
        ('downscaling_type', 'type', unicode),
        ('downscaling_id', 'type', unicode),
        ('calendar', 'type', shared.Calendar),
        ('supports', 'type', activity.Experiment),
        ('projects', 'type', unicode),

        ('inputs', 'cardinality', "0.N"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('outputs', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('downscaled_from', 'cardinality', "1.1"),
        ('meta', 'cardinality', "1.1"),
        ('downscaling_type', 'cardinality', "0.1"),
        ('downscaling_id', 'cardinality', "0.1"),
        ('calendar', 'cardinality', "1.1"),
        ('supports', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    activity.Ensemble: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('outputs', 'type', shared.DataSource),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('types', 'type', unicode),
        ('members', 'type', activity.EnsembleMember),
        ('supports', 'type', activity.Experiment),
        ('projects', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('outputs', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('types', 'cardinality', "1.N"),
        ('members', 'cardinality', "1.N"),
        ('supports', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    shared.ChangeProperty: (

        ('id', 'type', unicode),
        ('name', 'type', unicode),
        ('value', 'type', unicode),
        ('description', 'type', unicode),

        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    data.DataObject: (

        ('hierarchy_level', 'type', data.DataHierarchyLevel),
        ('source_simulation', 'type', unicode),
        ('description', 'type', unicode),
        ('keyword', 'type', unicode),
        ('restriction', 'type', data.DataRestriction),
        ('acronym', 'type', unicode),
        ('citations', 'type', shared.Citation),
        ('storage', 'type', data.DataStorage),
        ('child_object', 'type', data.DataObject),
        ('content', 'type', data.DataContent),
        ('geometry_model', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('purpose', 'type', unicode),
        ('extent', 'type', data.DataExtent),
        ('distribution', 'type', data.DataDistribution),
        ('parent_object', 'type', data.DataObject),
        ('properties', 'type', data.DataProperty),
        ('data_status', 'type', unicode),

        ('hierarchy_level', 'cardinality', "0.1"),
        ('source_simulation', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('keyword', 'cardinality', "0.1"),
        ('restriction', 'cardinality', "0.N"),
        ('acronym', 'cardinality', "0.1"),
        ('citations', 'cardinality', "0.N"),
        ('storage', 'cardinality', "0.N"),
        ('child_object', 'cardinality', "0.N"),
        ('content', 'cardinality', "0.N"),
        ('geometry_model', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('purpose', 'cardinality', "0.1"),
        ('extent', 'cardinality', "0.1"),
        ('distribution', 'cardinality', "0.1"),
        ('parent_object', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('data_status', 'cardinality', "0.1"),

    ),
    data.DataStorageFile: (

        ('modification_date', 'type', datetime.datetime),
        ('format', 'type', unicode),
        ('file_name', 'type', unicode),
        ('location', 'type', unicode),
        ('path', 'type', unicode),
        ('file_system', 'type', unicode),
        ('size', 'type', int),

        ('modification_date', 'cardinality', "0.1"),
        ('format', 'cardinality', "0.1"),
        ('file_name', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('path', 'cardinality', "0.1"),
        ('file_system', 'cardinality', "0.1"),
        ('size', 'cardinality', "0.1"),

    ),
    activity.EnsembleMember: (

        ('ensemble_ids', 'type', shared.StandardName),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('simulation', 'type', activity.Simulation),
        ('long_name', 'type', unicode),
        ('supports', 'type', activity.Experiment),
        ('ensemble', 'type', activity.Ensemble),
        ('projects', 'type', unicode),

        ('ensemble_ids', 'cardinality', "0.N"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('simulation', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('supports', 'cardinality', "0.N"),
        ('ensemble', 'cardinality', "0.1"),
        ('projects', 'cardinality', "0.N"),

    ),
    activity.SimulationRelationship: (

        ('direction', 'type', unicode),
        ('type', 'type', unicode),
        ('description', 'type', unicode),
        ('target', 'type', activity.SimulationRelationshipTarget),

        ('direction', 'cardinality', "1.1"),
        ('type', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('target', 'cardinality', "1.1"),

    ),
    data.DataDistribution: (

        ('access', 'type', unicode),
        ('fee', 'type', unicode),
        ('responsible_party', 'type', shared.ResponsibleParty),
        ('format', 'type', unicode),

        ('access', 'cardinality', "0.1"),
        ('fee', 'cardinality', "0.1"),
        ('responsible_party', 'cardinality', "0.1"),
        ('format', 'cardinality', "0.1"),

    ),
    shared.DocRelationshipTarget: (

        ('reference', 'type', shared.DocReference),

        ('reference', 'cardinality', "0.1"),

    ),
    software.ComponentProperty: (

        ('standard_names', 'type', unicode),
        ('sub_properties', 'type', software.ComponentProperty),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('is_represented', 'type', bool),
        ('long_name', 'type', unicode),
        ('citations', 'type', shared.Citation),
        ('grid', 'type', unicode),
        ('purpose', 'type', unicode),
        ('units', 'type', unicode),
        ('values', 'type', unicode),
        ('intent', 'type', unicode),

        ('standard_names', 'cardinality', "0.N"),
        ('sub_properties', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('is_represented', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('citations', 'cardinality', "0.N"),
        ('grid', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('units', 'cardinality', "0.1"),
        ('values', 'cardinality', "0.N"),
        ('intent', 'cardinality', "0.1"),

    ),
    activity.Simulation: (

        ('inputs', 'type', software.Coupling),
        ('simulation_id', 'type', unicode),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('control_simulation', 'type', activity.Simulation),
        ('spinup_simulation', 'type', activity.Simulation),
        ('spinup_date_range', 'type', shared.ClosedDateRange),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('restarts', 'type', data.DataObject),
        ('long_name', 'type', unicode),
        ('outputs', 'type', data.DataObject),
        ('authors', 'type', unicode),
        ('conformances', 'type', activity.Conformance),
        ('supports', 'type', activity.Experiment),
        ('calendar', 'type', shared.Calendar),
        ('projects', 'type', unicode),

        ('inputs', 'cardinality', "0.N"),
        ('simulation_id', 'cardinality', "0.1"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('control_simulation', 'cardinality', "0.1"),
        ('spinup_simulation', 'cardinality', "0.1"),
        ('spinup_date_range', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('restarts', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('outputs', 'cardinality', "0.N"),
        ('authors', 'cardinality', "0.1"),
        ('conformances', 'cardinality', "0.N"),
        ('supports', 'cardinality', "0.N"),
        ('calendar', 'cardinality', "1.1"),
        ('projects', 'cardinality', "0.N"),

    ),
    software.Timing: (

        ('units', 'type', unicode),
        ('end', 'type', datetime.datetime),
        ('rate', 'type', int),
        ('is_variable_rate', 'type', bool),
        ('start', 'type', datetime.datetime),

        ('units', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),
        ('rate', 'cardinality', "0.1"),
        ('is_variable_rate', 'cardinality', "0.1"),
        ('start', 'cardinality', "0.1"),

    ),
    quality.CimQuality: (

        ('meta', 'type', shared.DocMetaInfo),
        ('reports', 'type', quality.Report),

        ('meta', 'cardinality', "1.1"),
        ('reports', 'cardinality', "0.N"),

    ),
    activity.NumericalRequirement: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    activity.NumericalRequirementOption: (

        ('name', 'type', unicode),
        ('sub_options', 'type', activity.NumericalRequirementOption),
        ('id', 'type', unicode),
        ('relationship', 'type', unicode),
        ('description', 'type', unicode),

        ('name', 'cardinality', "1.1"),
        ('sub_options', 'cardinality', "0.N"),
        ('id', 'cardinality', "0.1"),
        ('relationship', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    activity.NumericalActivity: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('long_name', 'type', unicode),
        ('supports', 'type', activity.Experiment),
        ('projects', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('supports', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    shared.DataSource: (

        ('purpose', 'type', unicode),

        ('purpose', 'cardinality', "0.1"),

    ),
    grids.GridProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    shared.Standard: (

        ('version', 'type', unicode),
        ('name', 'type', unicode),
        ('description', 'type', unicode),

        ('version', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),

    ),
    software.TimeTransformation: (

        ('description', 'type', unicode),
        ('mapping_type', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('mapping_type', 'cardinality', "1.1"),

    ),
    shared.DocGenealogy: (

        ('relationships', 'type', shared.DocRelationship),

        ('relationships', 'cardinality', "0.N"),

    ),
    software.Deployment: (

        ('executable_arguments', 'type', unicode),
        ('description', 'type', unicode),
        ('parallelisation', 'type', software.Parallelisation),
        ('deployment_date', 'type', datetime.datetime),
        ('platform', 'type', shared.Platform),
        ('executable_name', 'type', unicode),

        ('executable_arguments', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('parallelisation', 'cardinality', "0.1"),
        ('deployment_date', 'cardinality', "0.1"),
        ('platform', 'cardinality', "0.1"),
        ('executable_name', 'cardinality', "0.1"),

    ),
    shared.Relationship: (

        ('direction', 'type', unicode),
        ('description', 'type', unicode),

        ('direction', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),

    ),
    shared.Machine: (

        ('operating_system', 'type', unicode),
        ('maximum_processors', 'type', int),
        ('name', 'type', unicode),
        ('cores_per_processor', 'type', int),
        ('interconnect', 'type', unicode),
        ('processor_type', 'type', unicode),
        ('system', 'type', unicode),
        ('libraries', 'type', unicode),
        ('location', 'type', unicode),
        ('vendor', 'type', unicode),
        ('type', 'type', unicode),
        ('description', 'type', unicode),

        ('operating_system', 'cardinality', "0.1"),
        ('maximum_processors', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('cores_per_processor', 'cardinality', "0.1"),
        ('interconnect', 'cardinality', "0.1"),
        ('processor_type', 'cardinality', "0.1"),
        ('system', 'cardinality', "0.1"),
        ('libraries', 'cardinality', "0.N"),
        ('location', 'cardinality', "0.1"),
        ('vendor', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    software.ModelComponent: (

        ('funding_sources', 'type', unicode),
        ('version', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('is_embedded', 'type', bool),
        ('short_name', 'type', unicode),
        ('previous_version', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('citations', 'type', shared.Citation),
        ('type', 'type', unicode),
        ('composition', 'type', software.Composition),
        ('coupling_framework', 'type', unicode),
        ('description', 'type', unicode),
        ('parent', 'type', software.Component),
        ('sub_components', 'type', software.Component),
        ('dependencies', 'type', software.EntryPoint),
        ('grid', 'type', grids.GridSpec),
        ('purpose', 'type', unicode),
        ('online_resource', 'type', unicode),
        ('timing', 'type', software.Timing),
        ('properties', 'type', software.ComponentProperty),
        ('types', 'type', unicode),
        ('language', 'type', software.ComponentLanguage),
        ('license', 'type', shared.License),
        ('release_date', 'type', datetime.datetime),
        ('code_access', 'type', unicode),
        ('activity', 'type', activity.Activity),

        ('funding_sources', 'cardinality', "0.N"),
        ('version', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('is_embedded', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('previous_version', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('citations', 'cardinality', "0.N"),
        ('type', 'cardinality', "0.1"),
        ('composition', 'cardinality', "0.1"),
        ('coupling_framework', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('parent', 'cardinality', "0.1"),
        ('sub_components', 'cardinality', "0.N"),
        ('dependencies', 'cardinality', "0.N"),
        ('grid', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('online_resource', 'cardinality', "0.1"),
        ('timing', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('types', 'cardinality', "1.N"),
        ('language', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('code_access', 'cardinality', "0.1"),
        ('activity', 'cardinality', "0.1"),

    ),
    activity.OutputRequirement: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "outputRequirement"),
    ),
    grids.GridTileResolutionType: (

        ('description', 'type', unicode),
        ('properties', 'type', grids.GridProperty),

        ('description', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    shared.Platform: (

        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('contacts', 'type', shared.ResponsibleParty),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('units', 'type', shared.MachineCompilerUnit),

        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('contacts', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('units', 'cardinality', "1.N"),

    ),
    data.DataTopic: (

        ('name', 'type', unicode),
        ('unit', 'type', unicode),
        ('description', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('unit', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    activity.MeasurementCampaign: (

        ('duration', 'type', int),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('projects', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('duration', 'cardinality', "1.1"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),

    ),
    shared.Calendar: (

        ('length', 'type', int),
        ('range', 'type', shared.DateRange),
        ('description', 'type', unicode),

        ('length', 'cardinality', "0.1"),
        ('range', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    software.CouplingEndpoint: (

        ('instance_id', 'type', unicode),
        ('data_source', 'type', shared.DataSource),
        ('properties', 'type', software.CouplingProperty),

        ('instance_id', 'cardinality', "0.1"),
        ('data_source', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    shared.DocRelationship: (

        ('direction', 'type', unicode),
        ('type', 'type', unicode),
        ('description', 'type', unicode),
        ('target', 'type', shared.DocRelationshipTarget),

        ('direction', 'cardinality', "1.1"),
        ('type', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('target', 'cardinality', "1.1"),

    ),
    grids.SimpleGridGeometry: (

        ('dim_order', 'type', unicode),
        ('num_dims', 'type', int),
        ('xcoords', 'type', grids.CoordinateList),
        ('is_mesh', 'type', bool),
        ('ycoords', 'type', grids.CoordinateList),
        ('zcoords', 'type', grids.CoordinateList),

        ('dim_order', 'cardinality', "0.1"),
        ('num_dims', 'cardinality', "1.1"),
        ('xcoords', 'cardinality', "1.1"),
        ('is_mesh', 'cardinality', "0.1"),
        ('ycoords', 'cardinality', "1.1"),
        ('zcoords', 'cardinality', "0.1"),

    ),
    shared.DocMetaInfo: (

        ('drs_keys', 'type', unicode),
        ('drs_path', 'type', unicode),
        ('create_date', 'type', datetime.datetime),
        ('language', 'type', unicode),
        ('genealogy', 'type', shared.DocGenealogy),
        ('author', 'type', shared.ResponsibleParty),
        ('sort_key', 'type', unicode),
        ('source_key', 'type', unicode),
        ('project', 'type', unicode),
        ('source', 'type', unicode),
        ('version', 'type', int),
        ('status', 'type', unicode),
        ('type_sort_key', 'type', unicode),
        ('update_date', 'type', datetime.datetime),
        ('external_ids', 'type', shared.StandardName),
        ('type', 'type', unicode),
        ('id', 'type', uuid.UUID),
        ('type_display_name', 'type', unicode),
        ('institute', 'type', unicode),

        ('drs_keys', 'cardinality', "0.N"),
        ('drs_path', 'cardinality', "0.1"),
        ('create_date', 'cardinality', "1.1"),
        ('language', 'cardinality', "1.1"),
        ('genealogy', 'cardinality', "0.1"),
        ('author', 'cardinality', "0.1"),
        ('sort_key', 'cardinality', "0.1"),
        ('source_key', 'cardinality', "0.1"),
        ('project', 'cardinality', "1.1"),
        ('source', 'cardinality', "1.1"),
        ('version', 'cardinality', "1.1"),
        ('status', 'cardinality', "0.1"),
        ('type_sort_key', 'cardinality', "0.1"),
        ('update_date', 'cardinality', "1.1"),
        ('external_ids', 'cardinality', "0.N"),
        ('type', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),
        ('type_display_name', 'cardinality', "0.1"),
        ('institute', 'cardinality', "0.1"),

        ('source', 'constant', "scripts"),
    ),
    activity.NumericalExperiment: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('generates', 'type', unicode),
        ('short_name', 'type', unicode),
        ('long_name', 'type', unicode),
        ('supports', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('measurement_campaigns', 'type', activity.MeasurementCampaign),
        ('meta', 'type', shared.DocMetaInfo),
        ('experiment_id', 'type', unicode),
        ('requirements', 'type', activity.NumericalRequirement),
        ('requires', 'type', activity.NumericalActivity),
        ('projects', 'type', unicode),
        ('description', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('generates', 'cardinality', "0.N"),
        ('short_name', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('supports', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('measurement_campaigns', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('experiment_id', 'cardinality', "0.1"),
        ('requirements', 'cardinality', "0.N"),
        ('requires', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),

    ),
    activity.PhysicalModification: (

        ('requirements', 'type', activity.NumericalRequirement),
        ('description', 'type', unicode),
        ('sources', 'type', shared.DataSource),
        ('frequency', 'type', unicode),
        ('is_conformant', 'type', bool),
        ('type', 'type', unicode),

        ('requirements', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('sources', 'cardinality', "0.N"),
        ('frequency', 'cardinality', "0.1"),
        ('is_conformant', 'cardinality', "1.1"),
        ('type', 'cardinality', "0.1"),

    ),
    activity.SimulationComposite: (

        ('funding_sources', 'type', unicode),
        ('child', 'type', activity.Simulation),
        ('rank', 'type', int),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('conformances', 'type', activity.Conformance),
        ('calendar', 'type', shared.Calendar),
        ('rationales', 'type', unicode),
        ('control_simulation', 'type', activity.Simulation),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('restarts', 'type', data.DataObject),
        ('supports', 'type', activity.Experiment),
        ('inputs', 'type', software.Coupling),
        ('simulation_id', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('outputs', 'type', data.DataObject),
        ('spinup_date_range', 'type', shared.ClosedDateRange),
        ('date_range', 'type', shared.DateRange),
        ('authors', 'type', unicode),
        ('projects', 'type', unicode),
        ('spinup_simulation', 'type', activity.Simulation),

        ('funding_sources', 'cardinality', "0.N"),
        ('child', 'cardinality', "0.N"),
        ('rank', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('conformances', 'cardinality', "0.N"),
        ('calendar', 'cardinality', "1.1"),
        ('rationales', 'cardinality', "0.N"),
        ('control_simulation', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('restarts', 'cardinality', "0.N"),
        ('supports', 'cardinality', "0.N"),
        ('inputs', 'cardinality', "0.N"),
        ('simulation_id', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('outputs', 'cardinality', "0.N"),
        ('spinup_date_range', 'cardinality', "0.1"),
        ('date_range', 'cardinality', "1.1"),
        ('authors', 'cardinality', "0.1"),
        ('projects', 'cardinality', "0.N"),
        ('spinup_simulation', 'cardinality', "0.1"),

    ),
    shared.License: (

        ('contact', 'type', unicode),
        ('description', 'type', unicode),
        ('is_unrestricted', 'type', bool),
        ('name', 'type', unicode),

        ('contact', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('is_unrestricted', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

    ),
    shared.Compiler: (

        ('name', 'type', unicode),
        ('language', 'type', unicode),
        ('version', 'type', unicode),
        ('environment_variables', 'type', unicode),
        ('type', 'type', unicode),
        ('options', 'type', unicode),

        ('name', 'cardinality', "1.1"),
        ('language', 'cardinality', "0.1"),
        ('version', 'cardinality', "1.1"),
        ('environment_variables', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('options', 'cardinality', "0.1"),

    ),
    software.Rank: (

        ('max', 'type', int),
        ('value', 'type', int),
        ('increment', 'type', int),
        ('min', 'type', int),

        ('max', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),
        ('increment', 'cardinality', "0.1"),
        ('min', 'cardinality', "0.1"),

    ),
    shared.StandardName: (

        ('is_open', 'type', bool),
        ('value', 'type', unicode),
        ('standards', 'type', shared.Standard),

        ('is_open', 'cardinality', "1.1"),
        ('value', 'cardinality', "1.1"),
        ('standards', 'cardinality', "0.N"),

    ),
    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------


    (shared.Property, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Property, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (grids.VerticalCoordinateList, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.VerticalCoordinateList, 'properties'): (

        ('type', grids.GridProperty),

        ('cardinality', "0.N"),

    ),
    (grids.VerticalCoordinateList, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.VerticalCoordinateList, 'form'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.VerticalCoordinateList, 'uom'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.VerticalCoordinateList, 'has_constant_offset'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),

    (software.Coupling, 'target'): (

        ('type', software.CouplingEndpoint),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'transformers'): (

        ('type', software.ProcessorComponent),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'is_fully_specified'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'connections'): (

        ('type', software.Connection),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'spatial_regriddings'): (

        ('type', software.SpatialRegridding),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'sources'): (

        ('type', software.CouplingEndpoint),

        ('cardinality', "1.N"),

    ),
    (software.Coupling, 'properties'): (

        ('type', software.CouplingProperty),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'purpose'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'time_profile'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'time_lag'): (

        ('type', software.TimeLag),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'time_transformation'): (

        ('type', software.TimeTransformation),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'priming'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),

    (data.DataStorage, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorage, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorage, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorage, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (activity.InitialCondition, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.InitialCondition, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.InitialCondition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.InitialCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.InitialCondition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.InitialCondition, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "initialCondition"),
    ),

    (shared.ResponsibleParty, 'url'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'role'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'address'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'organisation_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'individual_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'abbreviation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'email'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.CouplingProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.CouplingProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Composition, 'couplings'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.Composition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.EntryPoint, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (quality.Evaluation, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'did_pass'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'specification'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'specification_hyperlink'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'explanation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'type_hyperlink'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DocReference, 'id'): (

        ('type', uuid.UUID),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'external_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'changes'): (

        ('type', shared.Change),

        ('cardinality', "0.N"),

    ),
    (shared.DocReference, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'url'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'version'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (software.ConnectionProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ConnectionProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.ProcessorComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.ProcessorComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ProcessorComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.ComponentLanguage, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ComponentLanguage, 'properties'): (

        ('type', software.ComponentLanguageProperty),

        ('cardinality', "0.N"),

    ),

    (shared.RealCalendar, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.RealCalendar, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.RealCalendar, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),

    (data.DataRestriction, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (data.DataRestriction, 'restriction'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataRestriction, 'scope'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Citation, 'alternative_title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'date_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'collective_title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'organisation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'role'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataHierarchyLevel, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataHierarchyLevel, 'is_open'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (data.DataHierarchyLevel, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.LateralBoundaryCondition, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.LateralBoundaryCondition, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.LateralBoundaryCondition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.LateralBoundaryCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.LateralBoundaryCondition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.LateralBoundaryCondition, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "lateralBoundaryCondition"),
    ),

    (shared.DateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Daily360, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Daily360, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Daily360, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),

    (activity.ExperimentRelationship, 'target'): (

        ('type', activity.ExperimentRelationshipTarget),

        ('cardinality', "1.1"),

    ),
    (activity.ExperimentRelationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.ExperimentRelationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.ExperimentRelationship, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.SpatialRegriddingUserMethod, 'file'): (

        ('type', data.DataObject),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegriddingUserMethod, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (grids.GridMosaic, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'is_leaf'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'tile_count'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'has_congruent_tiles'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'mosaics'): (

        ('type', grids.GridMosaic),

        ('cardinality', "0.N"),

    ),
    (grids.GridMosaic, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (grids.GridMosaic, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'mosaic_count'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'tiles'): (

        ('type', grids.GridTile),

        ('cardinality', "0.N"),

    ),
    (grids.GridMosaic, 'mnemonic'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'extent'): (

        ('type', grids.GridExtent),

        ('cardinality', "0.1"),

    ),

    (data.DataExtentTemporal, 'end'): (

        ('type', datetime.date),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentTemporal, 'time_interval'): (

        ('type', data.DataExtentTimeInterval),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentTemporal, 'begin'): (

        ('type', datetime.date),

        ('cardinality', "0.1"),

    ),

    (software.SpatialRegriddingProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegriddingProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataExtent, 'geographical'): (

        ('type', data.DataExtentGeographical),

        ('cardinality', "1.1"),

    ),
    (data.DataExtent, 'temporal'): (

        ('type', data.DataExtentTemporal),

        ('cardinality', "1.1"),

    ),

    (grids.GridExtent, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridExtent, 'maximum_longitude'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridExtent, 'maximum_latitude'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridExtent, 'minimum_longitude'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridExtent, 'minimum_latitude'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (activity.Activity, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (grids.GridSpec, 'esm_exchange_grids'): (

        ('type', grids.GridMosaic),

        ('cardinality', "0.N"),

    ),
    (grids.GridSpec, 'esm_model_grids'): (

        ('type', grids.GridMosaic),

        ('cardinality', "0.N"),

    ),
    (grids.GridSpec, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),

    (shared.Change, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'author'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'details'): (

        ('type', shared.ChangeProperty),

        ('cardinality', "1.N"),

    ),

    (activity.SimulationRelationshipTarget, 'simulation'): (

        ('type', shared.DocReference),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRelationshipTarget, 'target'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Component, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.Component, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),

    (software.SpatialRegridding, 'properties'): (

        ('type', software.SpatialRegriddingProperty),

        ('cardinality', "0.N"),

    ),
    (software.SpatialRegridding, 'user_method'): (

        ('type', software.SpatialRegriddingUserMethod),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegridding, 'dimension'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegridding, 'standard_method'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (quality.Report, 'measure'): (

        ('type', quality.Measure),

        ('cardinality', "1.1"),

    ),
    (quality.Report, 'evaluator'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),
    (quality.Report, 'evaluation'): (

        ('type', quality.Evaluation),

        ('cardinality', "1.1"),

    ),
    (quality.Report, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),

    (shared.PerpetualPeriod, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.PerpetualPeriod, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.PerpetualPeriod, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),

    (data.DataStorageIp, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'protocol'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'host'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'file_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.ClosedDateRange, 'end'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.ClosedDateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ClosedDateRange, 'start'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),

    (activity.Conformance, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'sources'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'is_conformant'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),

    (data.DataProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataProperty, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.BoundaryCondition, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.BoundaryCondition, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.BoundaryCondition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.BoundaryCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.BoundaryCondition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.BoundaryCondition, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "boundaryCondition"),
    ),

    (software.ConnectionEndpoint, 'instance_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ConnectionEndpoint, 'properties'): (

        ('type', software.ConnectionProperty),

        ('cardinality', "0.N"),

    ),
    (software.ConnectionEndpoint, 'data_source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),

    (misc.DocumentSet, 'data'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (misc.DocumentSet, 'grids'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.N"),

    ),
    (misc.DocumentSet, 'model'): (

        ('type', software.ModelComponent),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (misc.DocumentSet, 'platform'): (

        ('type', shared.Platform),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'ensembles'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.N"),

    ),
    (misc.DocumentSet, 'simulation'): (

        ('type', activity.SimulationRun),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'experiment'): (

        ('type', activity.NumericalExperiment),

        ('cardinality', "0.1"),

    ),

    (software.StatisticalModelComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'timing'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.StatisticalModelComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.StatisticalModelComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (software.StatisticalModelComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Connection, 'target'): (

        ('type', software.ConnectionEndpoint),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'properties'): (

        ('type', software.ConnectionProperty),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'spatial_regridding'): (

        ('type', software.SpatialRegridding),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'priming'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'time_lag'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'sources'): (

        ('type', software.ConnectionEndpoint),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'time_profile'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'transformers'): (

        ('type', software.ProcessorComponent),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'time_transformation'): (

        ('type', software.TimeTransformation),

        ('cardinality', "0.1"),

    ),

    (activity.SpatioTemporalConstraint, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.SpatioTemporalConstraint, 'spatial_resolution'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "spatioTemporalConstraint"),
    ),
    (activity.SpatioTemporalConstraint, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SpatioTemporalConstraint, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),

    (data.DataExtentGeographical, 'north'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentGeographical, 'east'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentGeographical, 'west'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentGeographical, 'south'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),

    (grids.CoordinateList, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.CoordinateList, 'uom'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.CoordinateList, 'has_constant_offset'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),

    (software.TimeLag, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.TimeLag, 'value'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (shared.MachineCompilerUnit, 'compilers'): (

        ('type', shared.Compiler),

        ('cardinality', "0.N"),

    ),
    (shared.MachineCompilerUnit, 'machine'): (

        ('type', shared.Machine),

        ('cardinality', "1.1"),

    ),

    (activity.SimulationRun, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'model'): (

        ('type', software.ModelComponent),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (data.DataStorageDb, 'access_string'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'owner'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'table'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.Experiment, 'supports'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'measurement_campaigns'): (

        ('type', activity.MeasurementCampaign),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'requires'): (

        ('type', activity.NumericalActivity),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'generates'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (software.ComponentLanguageProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentLanguageProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataExtentTimeInterval, 'radix'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentTimeInterval, 'unit'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentTimeInterval, 'factor'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (quality.Measure, 'identification'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Measure, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Measure, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.ExperimentRelationshipTarget, 'numerical_experiment'): (

        ('type', activity.NumericalExperiment),

        ('cardinality', "0.1"),

    ),

    (shared.OpenDateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.OpenDateRange, 'end'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.OpenDateRange, 'start'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),

    (data.DataContent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataContent, 'aggregation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataContent, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataContent, 'topic'): (

        ('type', data.DataTopic),

        ('cardinality', "1.1"),

    ),

    (grids.GridTile, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'extent'): (

        ('type', grids.GridExtent),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'geometry_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'vertical_crs'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'zcoords'): (

        ('type', grids.VerticalCoordinateList),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'horizontal_resolution'): (

        ('type', grids.GridTileResolutionType),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'grid_north_pole'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'nx'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'discretization_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'simple_grid_geom'): (

        ('type', grids.SimpleGridGeometry),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'ny'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'area'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'horizontal_crs'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_conformal'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'cell_array'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'nz'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_regular'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'cell_ref_array'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'vertical_resolution'): (

        ('type', grids.GridTileResolutionType),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_terrain_following'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'coord_file'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'mnemonic'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_uniform'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'coordinate_pole'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'refinement_scheme'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'short_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Parallelisation, 'processes'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (software.Parallelisation, 'ranks'): (

        ('type', software.Rank),

        ('cardinality', "0.N"),

    ),

    (activity.DownscalingSimulation, 'downscaling_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'downscaling_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'downscaled_from'): (

        ('type', shared.DataSource),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (activity.Ensemble, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'outputs'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.Ensemble, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Ensemble, 'members'): (

        ('type', activity.EnsembleMember),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (shared.ChangeProperty, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ChangeProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ChangeProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ChangeProperty, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataObject, 'content'): (

        ('type', data.DataContent),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'data_status'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'acronym'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'hierarchy_level'): (

        ('type', data.DataHierarchyLevel),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'properties'): (

        ('type', data.DataProperty),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'distribution'): (

        ('type', data.DataDistribution),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'keyword'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'geometry_model'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (data.DataObject, 'source_simulation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'extent'): (

        ('type', data.DataExtent),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'child_object'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'restriction'): (

        ('type', data.DataRestriction),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'parent_object'): (

        ('type', data.DataObject),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'storage'): (

        ('type', data.DataStorage),

        ('cardinality', "0.N"),

    ),

    (data.DataStorageFile, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'file_system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'file_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (activity.EnsembleMember, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'ensemble'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.EnsembleMember, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'ensemble_ids'): (

        ('type', shared.StandardName),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (activity.SimulationRelationship, 'target'): (

        ('type', activity.SimulationRelationshipTarget),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRelationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRelationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRelationship, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (data.DataDistribution, 'access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataDistribution, 'fee'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataDistribution, 'responsible_party'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),
    (data.DataDistribution, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DocRelationshipTarget, 'reference'): (

        ('type', shared.DocReference),

        ('cardinality', "0.1"),

    ),

    (software.ComponentProperty, 'values'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'grid'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'sub_properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'standard_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'intent'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ComponentProperty, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'is_represented'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),

    (activity.Simulation, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.Simulation, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Simulation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),

    (software.Timing, 'is_variable_rate'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'end'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'start'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'rate'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (quality.CimQuality, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (quality.CimQuality, 'reports'): (

        ('type', quality.Report),

        ('cardinality', "0.N"),

    ),

    (activity.NumericalRequirement, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalRequirement, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirement, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalRequirement, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),

    (activity.NumericalRequirementOption, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirementOption, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirementOption, 'relationship'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirementOption, 'sub_options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalRequirementOption, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (activity.NumericalActivity, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalActivity, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalActivity, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalActivity, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (shared.DataSource, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (grids.GridProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Standard, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Standard, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Standard, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.TimeTransformation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.TimeTransformation, 'mapping_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.DocGenealogy, 'relationships'): (

        ('type', shared.DocRelationship),

        ('cardinality', "0.N"),

    ),

    (software.Deployment, 'executable_arguments'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.Deployment, 'parallelisation'): (

        ('type', software.Parallelisation),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'deployment_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'executable_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'platform'): (

        ('type', shared.Platform),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Relationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Relationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.Machine, 'libraries'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.Machine, 'system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'cores_per_processor'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Machine, 'maximum_processors'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'vendor'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'operating_system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'processor_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'interconnect'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.ModelComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'activity'): (

        ('type', activity.Activity),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.ModelComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (software.ModelComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ModelComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'timing'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.OutputRequirement, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.OutputRequirement, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.OutputRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.OutputRequirement, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.OutputRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.OutputRequirement, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "outputRequirement"),
    ),

    (grids.GridTileResolutionType, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTileResolutionType, 'properties'): (

        ('type', grids.GridProperty),

        ('cardinality', "0.N"),

    ),

    (shared.Platform, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Platform, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (shared.Platform, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Platform, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Platform, 'units'): (

        ('type', shared.MachineCompilerUnit),

        ('cardinality', "1.N"),

    ),
    (shared.Platform, 'contacts'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (data.DataTopic, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataTopic, 'unit'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataTopic, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.MeasurementCampaign, 'duration'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (activity.MeasurementCampaign, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (shared.Calendar, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Calendar, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),
    (shared.Calendar, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.CouplingEndpoint, 'instance_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.CouplingEndpoint, 'properties'): (

        ('type', software.CouplingProperty),

        ('cardinality', "0.N"),

    ),
    (software.CouplingEndpoint, 'data_source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),

    (shared.DocRelationship, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocRelationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocRelationship, 'target'): (

        ('type', shared.DocRelationshipTarget),

        ('cardinality', "1.1"),

    ),
    (shared.DocRelationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (grids.SimpleGridGeometry, 'ycoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "1.1"),

    ),
    (grids.SimpleGridGeometry, 'is_mesh'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.SimpleGridGeometry, 'zcoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "0.1"),

    ),
    (grids.SimpleGridGeometry, 'xcoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "1.1"),

    ),
    (grids.SimpleGridGeometry, 'dim_order'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.SimpleGridGeometry, 'num_dims'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (shared.DocMetaInfo, 'drs_path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'id'): (

        ('type', uuid.UUID),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'source'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "scripts"),
    ),
    (shared.DocMetaInfo, 'drs_keys'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'source_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'version'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'status'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'sort_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'genealogy'): (

        ('type', shared.DocGenealogy),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'type_display_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'project'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'author'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'external_ids'): (

        ('type', shared.StandardName),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'type_sort_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'create_date'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'institute'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'update_date'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'language'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (activity.NumericalExperiment, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'supports'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalExperiment, 'generates'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalExperiment, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'experiment_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'requires'): (

        ('type', activity.NumericalActivity),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'measurement_campaigns'): (

        ('type', activity.MeasurementCampaign),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.PhysicalModification, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.PhysicalModification, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.PhysicalModification, 'is_conformant'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (activity.PhysicalModification, 'sources'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.PhysicalModification, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (activity.PhysicalModification, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.SimulationComposite, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'child'): (

        ('type', activity.Simulation),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'rank'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),

    (shared.License, 'contact'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.License, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.License, 'is_unrestricted'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (shared.License, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Compiler, 'options'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'language'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'version'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Compiler, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Compiler, 'environment_variables'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Rank, 'increment'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Rank, 'value'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Rank, 'max'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Rank, 'min'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (shared.StandardName, 'is_open'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (shared.StandardName, 'standards'): (

        ('type', shared.Standard),

        ('cardinality', "0.N"),

    ),
    (shared.StandardName, 'value'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
}

# Count of class constraints.
TOTAL_CONSTRAINTS = sum(len(CONSTRAINTS[c]) for c in CLASSES)

# ------------------------------------------------
# Type help text.
# ------------------------------------------------
HELP = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    shared: "Shared types that might be imported from other packages within the ontology.",
    data: "Types that describe output that climate models emit.",
    grids: "Types that describe the grids that climate models plot.",
    quality: "Types that describe the quailty of output that climate models emit.",
    misc: "Miscellaneous types.",
    activity: "Types that describe context against which climate models are run.",
    software: "Types that describe the climate models software.",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    shared.DocReference: """
        A reference to another cim entity.

    """,
    shared.DateRange: """
        Creates and returns instance of date_range class.

    """,
    shared.Change: """
        A description of [a set of] changes applied at a particular time, by a particular party, to a particular unit of metadata.

    """,
    shared.OpenDateRange: """
        A date range without a specified start and/or end point.

    """,
    shared.DocRelationship: """
        Contains the set of relationships supported by a Document.

    """,
    shared.Daily360: """
        Creates and returns instance of daily_360 class.

    """,
    shared.Standard: """
        Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """,
    shared.RealCalendar: """
        Creates and returns instance of real_calendar class.

    """,
    shared.DocRelationshipTarget: """
        Creates and returns instance of doc_relationship_target class.

    """,
    shared.Citation: """
        An academic reference to published work.

    """,
    shared.Property: """
        A simple name/value pair representing a property of some entity or other.

    """,
    shared.License: """
        A description of a license restricting access to a unit of data or software.

    """,
    shared.Machine: """
        A description of a machine used by a particular platform.

    """,
    shared.DataSource: """
        A DataSource can be realised by either a DataObject (file), a DataContent (variable), a Component (model), or a ComponentProperty (variable); all of those can supply data.

    """,
    shared.DocGenealogy: """
        A record of a document's history. A genealogy element contains a textual description and a set of relationships. Each relationship has a type and a reference to some target. There are different relationships for different document types.

    """,
    shared.MachineCompilerUnit: """
        Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.

    """,
    shared.Relationship: """
        A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document's genealogy.

    """,
    shared.Compiler: """
        A description of a compiler used on a particular platform.

    """,
    shared.PerpetualPeriod: """
        Creates and returns instance of perpetual_period class.

    """,
    shared.Platform: """
        A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.

    """,
    shared.ClosedDateRange: """
        A date range with specified start and end points.

    """,
    shared.Calendar: """
        Describes a method of calculating a span of dates.

    """,
    shared.ResponsibleParty: """
        A person/organsiation responsible for some aspect of a climate science artefact.

    """,
    shared.DocMetaInfo: """
        Encapsulates document meta information.

    """,
    shared.ChangeProperty: """
        A description of a single change applied to a single target.  Every ChangeProperty has a description, and may also have a name from a controlled vocabulary and a value.

    """,
    shared.StandardName: """
        Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """,
    data.DataDistribution: """
        Describes how a DataObject is distributed.

    """,
    data.DataProperty: """
        A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.

    """,
    data.DataStorageFile: """
        Contains attributes to describe a DataObject stored as a single file.

    """,
    data.DataExtentTemporal: """
        A data object temporal extent represents the temporal coverage associated with a data object.

    """,
    data.DataExtentTimeInterval: """
        A data object temporal extent represents the temporal coverage associated with a data object.

    """,
    data.DataRestriction: """
        An access or use restriction on some element of the DataObject actual data.

    """,
    data.DataStorage: """
        Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.

    """,
    data.DataExtentGeographical: """
        A data object geographical extent represents the geographical coverage associated with a data object.

    """,
    data.DataObject: """
        A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.

    """,
    data.DataHierarchyLevel: """
        The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.

    """,
    data.DataExtent: """
        A data object extent represents the geographical and temporal coverage associated with a data object.

    """,
    data.DataContent: """
        The contents of the data object; like ISO: MD_ContentInformation.

    """,
    data.DataTopic: """
        Describes the content of a data object: the variable name, units, etc.

    """,
    data.DataStorageDb: """
        Contains attributes to describe a DataObject stored as a database file.

    """,
    data.DataStorageIp: """
        Contains attributes to describe a DataObject stored as a database file.

    """,
    grids.GridExtent: """
        DataType for recording the geographic extent of a gridMosaic or gridTile.

    """,
    grids.GridTileResolutionType: """
        Provides a description and set of named properties for the horizontal or vertical resolution.

    """,
    grids.GridProperty: """
        Creates and returns instance of grid_property class.

    """,
    grids.SimpleGridGeometry: """
        SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type.

    """,
    grids.GridSpec: """
        This is a container class for GridSpec objects. A GridSpec object can contain one or more esmModelGrid objects, and one or more esmExchangeGrid objects. These objects may be serialised to one or possibly several files according to taste. Since GridSpec is sub-typed from GML's AbstractGeometryType it can, and should, be identified using a gml:id attribute.

    """,
    grids.CoordinateList: """
        The CoordList type may be used to specify a list of coordinates, typically for the purpose of defining coordinates along the X, Y or Z axes. The length of the coordinate list is given by the attribute of that name. This may be used by software to allocate memory in advance of storing the coordinate values. The hasConstantOffset attribute may be used to indicate that the coordinate list consists of values with constant offset (spacing). In this case only the first coordinate value and the offset (spacing) value need to be specified; however, the length attribute must still define the final as-built size of the coordinate list.

    """,
    grids.GridTile: """
        The GridTile class is used to model an individual grid tile contained within a grid mosaic. A GridTile consists of an array of grid cells which may be defined in one of four ways: 1) for simple grids, by use of the SimpleGridGeometry data type; 2) by defining an array of GridCell objects; 3) by specifying an array of references to externally defined GridCell objects; or 4) by specifying a URI to a remote data file containing the grid cell definitions.  For all but the simplest grid tiles, it is envisaged that method 4 above will be the most frequently used option. However, it should be remembered that the CIM is primarily concerned with encoding climate model metadata. Specifying the coordinates of individual grid tiles and cells will most likely not be required as part of such metadata descriptions.  A GridTile object is associated with a geodetic or projected CRS via the horizontalCRS property, and with a vertical CRS via the verticalCRS property.

    """,
    grids.GridMosaic: """
        The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.

    """,
    grids.VerticalCoordinateList: """
        There are some specific attributes that are associated with vertical coordinates.

    """,
    quality.Measure: """
        Creates and returns instance of measure class.

    """,
    quality.Report: """
        Creates and returns instance of report class.

    """,
    quality.CimQuality: """
        The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.

    """,
    quality.Evaluation: """
        Creates and returns instance of evaluation class.

    """,
    misc.DocumentSet: """
        Represents a bundled set of documents.

    """,
    activity.Experiment: """
        An experiment might be an activity which is both observational and numerical in focus, for example, a measurement campaign and numerical experiments for an alpine experiment.  It is a place for the scientific description of the reason why an experiment was made.

    """,
    activity.SimulationRelationship: """
        Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """,
    activity.DownscalingSimulation: """
        A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """,
    activity.LateralBoundaryCondition: """
        A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

    """,
    activity.NumericalRequirement: """
        A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.

    """,
    activity.EnsembleMember: """
        A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a 'simulation composite'.  The 'parent' simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """,
    activity.InitialCondition: """
        An initial condition is a numerical requirement on a model prognostic variable value at time zero.

    """,
    activity.NumericalActivity: """
        Creates and returns instance of numerical_activity class.

    """,
    activity.Simulation: """
        A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """,
    activity.ExperimentRelationship: """
        Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.

    """,
    activity.ExperimentRelationshipTarget: """
        Creates and returns instance of experiment_relationship_target class.

    """,
    activity.NumericalRequirementOption: """
        A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that 'parent' requirement would have three 'child' RequirmentOptions (each of one with the XOR optionRelationship).

    """,
    activity.Activity: """
        An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.

    """,
    activity.SimulationRelationshipTarget: """
        Creates and returns instance of simulation_relationship_target class.

    """,
    activity.SpatioTemporalConstraint: """
        Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """,
    activity.OutputRequirement: """
        Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """,
    activity.MeasurementCampaign: """
        Creates and returns instance of measurement_campaign class.

    """,
    activity.Conformance: """
        A conformance class maps how a configured model component met a specific numerical requirement.  For example, for a double CO2 boundary condition, a model component might read a CO2 dataset in which CO2 has been doubled, or it might modify a parameterisation (presumably with a factor of two somewhere).  So, the conformance links a requirement to a DataSource (which can be either an actual DataObject or a property of a model component).  In some cases a model/simulation may _naturally_ conform to a requirement.  In this case there would be no reference to a DataSource but the conformant attribute would be true.  If something is purpopsefully non-conformant then the conformant attribute would be false.

    """,
    activity.BoundaryCondition: """
        A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

    """,
    activity.Ensemble: """
        An ensemble is made up of two or more simulations which are to be compared against each other to create ensemble statistics. Ensemble members can differ in terms of initial conditions, physical parameterisation and the model used. An ensemble bundles together sets of ensembleMembers, all of which reference the same Simulation(Run) and include one or more changes.

    """,
    activity.SimulationRun: """
        A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.

    """,
    activity.PhysicalModification: """
        Physical modification is the implementation of a boundary condition numerical requirement that is achieved within the model code rather than from some external source file. It  might include, for example,  a specific rate constant within a chemical reaction, or coefficient value(s) in a parameterisation.  For example, one might require a numerical experiment where specific chemical reactions were turned off - e.g. no heterogeneous chemistry.

    """,
    activity.SimulationComposite: """
        A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of 'child' simulations aggregated together to form a 'simulation composite'.  The 'parent' simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.

    """,
    activity.NumericalExperiment: """
        A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.

    """,
    software.Coupling: """
        A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.

    """,
    software.Parallelisation: """
        Describes how a deployment has been parallelised across a computing platform.

    """,
    software.SpatialRegridding: """
        Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

    """,
    software.EntryPoint: """
        Describes a function or subroutine of a SoftwareComponent. BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model. Currently, a very basic schedule can be approximated by using the 'proceeds' and 'follows' attributes, however a more complete system is required for full BFG compatibility. Every EntryPoint can have a set of arguments associated with it. These reference (previously defined) ComponentProperties.

    """,
    software.ProcessorComponent: """
        A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

    """,
    software.ConnectionProperty: """
        A ConnectionProperty is a name/value pair used to specify OASIS-specific properties.

    """,
    software.StatisticalModelComponent: """
        Creates and returns instance of statistical_model_component class.

    """,
    software.Composition: """
        The set of Couplings used by a Component. Couplings can only occur between child components. That is, a composition must belong to an ancestor component of the components whose fields are being connected.

    """,
    software.Timing: """
        Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).

    """,
    software.ComponentLanguage: """
        Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.

    """,
    software.SpatialRegriddingUserMethod: """
        Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

    """,
    software.ComponentLanguageProperty: """
        This provides a place to include language-specific information. Every property is basically a name/value pair, where the names are things like: moduleName, reservedUnits, reservedNames (these are all examples of Fortran-specific properties).

    """,
    software.SpatialRegriddingProperty: """
        Used for OASIS-specific regridding information (ie: masked, order, normalisation, etc.)

    """,
    software.ComponentProperty: """
        ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.

    """,
    software.TimeTransformation: """
        The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

    """,
    software.Deployment: """
        Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.

    """,
    software.Component: """
        A SofwareComponent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested 'child' components. Every component can have 'componentProperties' which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component's composition must be owned by that component or a child of that component; child components cannot couple together their parents' properties.

    """,
    software.ModelComponent: """
        A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

    """,
    software.Rank: """
        Creates and returns instance of rank class.

    """,
    software.CouplingEndpoint: """
        The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

    """,
    software.TimeLag: """
        The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

    """,
    software.Connection: """
        A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.

    """,
    software.ConnectionEndpoint: """
        The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

    """,
    software.CouplingProperty: """
        A CouplingProperty is a name/value pair used to specify OASIS-specific properties.

    """,

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (shared.DocReference, 'id'):
        "The ID of the element being referenced.",
    (shared.DocReference, 'description'):
        "A description of the element being referenced, in the context of the current class.",
    (shared.DocReference, 'changes'):
        "An optional description of how the item being referenced has been modified.  This is particularly useful for dealing with Ensembles (a set of simulations where something about each simulation has changed) or Conformances.",
    (shared.DocReference, 'url'):
        "A URL associated witht he document reference.",
    (shared.DocReference, 'type'):
        "The type of the element being referenced.",
    (shared.DocReference, 'name'):
        "The name of the element being referenced.",
    (shared.DocReference, 'external_id'):
        "A non-CIM (non-GUID) id used to reference the element in question.",
    (shared.DocReference, 'version'):
        "The version of the element being referenced.",
    (shared.DateRange, 'duration'):
        None,
    (shared.Change, 'description'):
        None,
    (shared.Change, 'name'):
        "A mnemonic for describing a particular change.",
    (shared.Change, 'details'):
        None,
    (shared.Change, 'author'):
        "The person that made the change.",
    (shared.Change, 'date'):
        "The date the change was implemented.",
    (shared.Change, 'type'):
        None,
    (shared.OpenDateRange, 'end'):
        None,
    (shared.OpenDateRange, 'start'):
        None,
    (shared.DocRelationship, 'type'):
        None,
    (shared.DocRelationship, 'target'):
        None,
    (shared.Standard, 'version'):
        "The version of the standard",
    (shared.Standard, 'description'):
        "The version of the standard",
    (shared.Standard, 'name'):
        "The name of the standard",
    (shared.DocRelationshipTarget, 'reference'):
        None,
    (shared.Citation, 'alternative_title'):
        None,
    (shared.Citation, 'date_type'):
        None,
    (shared.Citation, 'collective_title'):
        None,
    (shared.Citation, 'organisation'):
        None,
    (shared.Citation, 'location'):
        None,
    (shared.Citation, 'role'):
        None,
    (shared.Citation, 'date'):
        None,
    (shared.Citation, 'title'):
        None,
    (shared.Citation, 'type'):
        None,
    (shared.Property, 'name'):
        None,
    (shared.Property, 'value'):
        None,
    (shared.License, 'contact'):
        "The point of contact for access to this artifact; may be either a person or an institution.",
    (shared.License, 'name'):
        "The name that the license goes by (ie: 'GPL')",
    (shared.License, 'is_unrestricted'):
        "If unrestricted='true' then the artifact can be downloaded with no restrictions (ie: there are no administrative steps for the user to deal with; code or data can be downloaded and used directly).",
    (shared.License, 'description'):
        "A textual description of the license; might be the full text of the license, more likely to be a brief summary",
    (shared.Machine, 'libraries'):
        "The libraries residing on this machine.",
    (shared.Machine, 'system'):
        None,
    (shared.Machine, 'cores_per_processor'):
        None,
    (shared.Machine, 'location'):
        None,
    (shared.Machine, 'type'):
        None,
    (shared.Machine, 'operating_system'):
        None,
    (shared.Machine, 'maximum_processors'):
        None,
    (shared.Machine, 'vendor'):
        None,
    (shared.Machine, 'description'):
        None,
    (shared.Machine, 'name'):
        None,
    (shared.Machine, 'processor_type'):
        None,
    (shared.Machine, 'interconnect'):
        None,
    (shared.DataSource, 'purpose'):
        None,
    (shared.DocGenealogy, 'relationships'):
        None,
    (shared.MachineCompilerUnit, 'compilers'):
        None,
    (shared.MachineCompilerUnit, 'machine'):
        None,
    (shared.Relationship, 'description'):
        None,
    (shared.Relationship, 'direction'):
        None,
    (shared.Compiler, 'language'):
        None,
    (shared.Compiler, 'version'):
        None,
    (shared.Compiler, 'name'):
        None,
    (shared.Compiler, 'environment_variables'):
        "The set of environment_variables used during compilation (recorded here as a single string rather than separate elements)",
    (shared.Compiler, 'options'):
        "The set of options used during compilation (recorded here as a single string rather than separate elements)",
    (shared.Compiler, 'type'):
        None,
    (shared.Platform, 'meta'):
        None,
    (shared.Platform, 'units'):
        None,
    (shared.Platform, 'contacts'):
        None,
    (shared.Platform, 'description'):
        None,
    (shared.Platform, 'long_name'):
        None,
    (shared.Platform, 'short_name'):
        None,
    (shared.ClosedDateRange, 'end'):
        "End date is optional becuase the length of a ClosedDateRange can be calculated from the StartDate plus the Duration element.",
    (shared.ClosedDateRange, 'start'):
        None,
    (shared.Calendar, 'range'):
        None,
    (shared.Calendar, 'description'):
        "Describes the finer details of the calendar, in case they are not-obvious.  For example, if an experiment has changing conditions within it (ie: 1% CO2 increase until 2100, then hold fixed for the remaining period of the  experment)",
    (shared.Calendar, 'length'):
        None,
    (shared.ResponsibleParty, 'url'):
        None,
    (shared.ResponsibleParty, 'individual_name'):
        None,
    (shared.ResponsibleParty, 'abbreviation'):
        None,
    (shared.ResponsibleParty, 'organisation_name'):
        None,
    (shared.ResponsibleParty, 'address'):
        None,
    (shared.ResponsibleParty, 'role'):
        None,
    (shared.ResponsibleParty, 'email'):
        None,
    (shared.DocMetaInfo, 'status'):
        "Document status.",
    (shared.DocMetaInfo, 'type_sort_key'):
        "Document type sort key.",
    (shared.DocMetaInfo, 'drs_path'):
        "DRS related path to support documents with datasets.",
    (shared.DocMetaInfo, 'source'):
        "Application that created the instance.",
    (shared.DocMetaInfo, 'type_display_name'):
        "Document type display name.",
    (shared.DocMetaInfo, 'language'):
        "Language with which instance is associated with.",
    (shared.DocMetaInfo, 'drs_keys'):
        "DRS related keys to support correlation of documents with datasets.",
    (shared.DocMetaInfo, 'institute'):
        "Name of institute with which instance is associated with.",
    (shared.DocMetaInfo, 'source_key'):
        "Key of application that created the instance.",
    (shared.DocMetaInfo, 'author'):
        "Associated document author.",
    (shared.DocMetaInfo, 'update_date'):
        "Date upon which the instance was last updated",
    (shared.DocMetaInfo, 'external_ids'):
        "Set of identifiers used to reference the document by external parties.",
    (shared.DocMetaInfo, 'sort_key'):
        "Document sort key.",
    (shared.DocMetaInfo, 'type'):
        "Document ontology type.",
    (shared.DocMetaInfo, 'version'):
        "Document version identifier.",
    (shared.DocMetaInfo, 'create_date'):
        "Date upon which the instance was created",
    (shared.DocMetaInfo, 'project'):
        "Name of project with which instance is associated with.",
    (shared.DocMetaInfo, 'genealogy'):
        "Specifies the relationship of this document with another document. Various relationship types (depending on the type of document; ie: simulation, component, etc.) are supported.",
    (shared.DocMetaInfo, 'id'):
        "Universal document identifier.",
    (shared.ChangeProperty, 'description'):
        "A text description of the change.  May be used in addition to, or instead of, the more formal description provided by the 'value' attribute.",
    (shared.ChangeProperty, 'id'):
        None,
    (shared.StandardName, 'is_open'):
        None,
    (shared.StandardName, 'value'):
        None,
    (shared.StandardName, 'standards'):
        "Details of the standard being used.",
    (data.DataDistribution, 'responsible_party'):
        None,
    (data.DataDistribution, 'format'):
        None,
    (data.DataDistribution, 'access'):
        None,
    (data.DataDistribution, 'fee'):
        None,
    (data.DataProperty, 'description'):
        None,
    (data.DataStorageFile, 'file_name'):
        None,
    (data.DataStorageFile, 'path'):
        None,
    (data.DataStorageFile, 'file_system'):
        None,
    (data.DataExtentTemporal, 'time_interval'):
        None,
    (data.DataExtentTemporal, 'begin'):
        None,
    (data.DataExtentTemporal, 'end'):
        None,
    (data.DataExtentTimeInterval, 'unit'):
        None,
    (data.DataExtentTimeInterval, 'factor'):
        None,
    (data.DataExtentTimeInterval, 'radix'):
        None,
    (data.DataRestriction, 'license'):
        "The thing (data or metadata, access or use) that this restriction is applied to.",
    (data.DataRestriction, 'scope'):
        "The thing (data or metadata, access or use) that this restriction is applied to.",
    (data.DataRestriction, 'restriction'):
        "The thing (data or metadata, access or use) that this restriction is applied to.",
    (data.DataStorage, 'format'):
        None,
    (data.DataStorage, 'size'):
        None,
    (data.DataStorage, 'modification_date'):
        None,
    (data.DataStorage, 'location'):
        None,
    (data.DataExtentGeographical, 'west'):
        None,
    (data.DataExtentGeographical, 'south'):
        None,
    (data.DataExtentGeographical, 'east'):
        None,
    (data.DataExtentGeographical, 'north'):
        None,
    (data.DataObject, 'distribution'):
        None,
    (data.DataObject, 'geometry_model'):
        None,
    (data.DataObject, 'purpose'):
        None,
    (data.DataObject, 'content'):
        "The content of a DataObject corresponds to a variable (in THREDDS, ...etc.)",
    (data.DataObject, 'source_simulation'):
        None,
    (data.DataObject, 'keyword'):
        None,
    (data.DataObject, 'data_status'):
        None,
    (data.DataObject, 'acronym'):
        None,
    (data.DataObject, 'meta'):
        None,
    (data.DataObject, 'extent'):
        None,
    (data.DataObject, 'properties'):
        None,
    (data.DataObject, 'description'):
        None,
    (data.DataObject, 'hierarchy_level'):
        None,
    (data.DataObject, 'storage'):
        None,
    (data.DataObject, 'restriction'):
        None,
    (data.DataObject, 'parent_object'):
        None,
    (data.DataObject, 'citations'):
        None,
    (data.DataObject, 'child_object'):
        None,
    (data.DataHierarchyLevel, 'is_open'):
        None,
    (data.DataHierarchyLevel, 'value'):
        "What is the name of the specific HierarchyLevel this DataObject is being organised at (ie: if the HierarchyLevel is 'run' then the name might be the runid).",
    (data.DataHierarchyLevel, 'name'):
        "What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.",
    (data.DataExtent, 'geographical'):
        None,
    (data.DataExtent, 'temporal'):
        None,
    (data.DataContent, 'topic'):
        None,
    (data.DataContent, 'aggregation'):
        "Describes how the content has been aggregated together: sum, min, mean, max, ...",
    (data.DataContent, 'frequency'):
        "Describes the frequency of the data content: daily, hourly, ...",
    (data.DataTopic, 'unit'):
        None,
    (data.DataTopic, 'description'):
        None,
    (data.DataTopic, 'name'):
        None,
    (data.DataStorageDb, 'owner'):
        None,
    (data.DataStorageDb, 'access_string'):
        None,
    (data.DataStorageDb, 'table'):
        None,
    (data.DataStorageDb, 'name'):
        None,
    (data.DataStorageIp, 'protocol'):
        None,
    (data.DataStorageIp, 'file_name'):
        None,
    (data.DataStorageIp, 'path'):
        None,
    (data.DataStorageIp, 'host'):
        None,
    (grids.GridExtent, 'units'):
        None,
    (grids.GridExtent, 'minimum_longitude'):
        None,
    (grids.GridExtent, 'minimum_latitude'):
        None,
    (grids.GridExtent, 'maximum_latitude'):
        None,
    (grids.GridExtent, 'maximum_longitude'):
        None,
    (grids.GridTileResolutionType, 'description'):
        "A description of the resolution.",
    (grids.GridTileResolutionType, 'properties'):
        None,
    (grids.SimpleGridGeometry, 'xcoords'):
        "X-Co-ordinates",
    (grids.SimpleGridGeometry, 'dim_order'):
        None,
    (grids.SimpleGridGeometry, 'ycoords'):
        "Y-Co-ordinates",
    (grids.SimpleGridGeometry, 'is_mesh'):
        None,
    (grids.SimpleGridGeometry, 'zcoords'):
        "Z-Co-ordinates",
    (grids.SimpleGridGeometry, 'num_dims'):
        None,
    (grids.GridSpec, 'esm_exchange_grids'):
        None,
    (grids.GridSpec, 'meta'):
        None,
    (grids.GridSpec, 'esm_model_grids'):
        None,
    (grids.CoordinateList, 'uom'):
        "Units of measure used by the coordinates.",
    (grids.CoordinateList, 'has_constant_offset'):
        "Set to true if coordinates in the built array have constant offset.",
    (grids.CoordinateList, 'length'):
        "Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used.",
    (grids.GridTile, 'geometry_type'):
        "Indicates the geometric figure used to approximate the figure of the Earth, e.g. 'sphere'.",
    (grids.GridTile, 'zcoords'):
        "This optional property may be used to specify the vertical coordinates (e.g. heights or model levels) at which a grid tile is utilised or realised. In the case of simple grid tiles the equivalent zcoords property on the SimpleGridGeometry data type would be used instead. The current property is intended to be used when the horizontal grid coordinates are defined by one of the other methods.",
    (grids.GridTile, 'horizontal_resolution'):
        "Provides an indication of the approximate spatial sampling size of the grid tile, i.e. the size of the underlying grid cells. (Note: the maximum spatial resolution of the grid is twice the sampling size (e.g. 2 km for a 1 km x 1 km grid pitch).",
    (grids.GridTile, 'id'):
        "Specifies an identifer for a grid tile that is unique within its parent grid mosaic. It is not required for this identifier to be unique either across all mosaics in a GridSpec or across all GridSpecs, though if that were the case it would not be detrimental.",
    (grids.GridTile, 'area'):
        "gml:MeasureType:Specifies the area of the grid tile in the units defined by the uom attribute that is attached to the GML MeasureType data type.",
    (grids.GridTile, 'is_conformal'):
        "This property is used to indicate if the grid tile is conformal, i.e. angle-preserving. If so, angles measured on the grid are equal to the equivalent angles on the Earth.",
    (grids.GridTile, 'cell_array'):
        "GridCellArray:This property may be used to specify an array of grid cell definitions which together define the coordinate geometry of a grid tile. Depending on context, any of the existing sub-types of GridCell may be used. Mixing types is, however, not currently permitted.",
    (grids.GridTile, 'is_regular'):
        "If true, indicates that the horizontal coordinates of the grid can be defined using 1D arrays (vectors). This means that grid node locations are defined by the cartesian product of the X/Lon and Y/Lat coordinate vectors. It also means that grid cells are logically rectangular (they may also be physically rectangular in the case of projected coordinates).",
    (grids.GridTile, 'cell_ref_array'):
        "GridCellArray:This property may be used to define the coordinate geometry of a grid tile by specifying an array of references to remotely defined grid cells. Depending on context, any of the existing sub-types of GridCell may be referenced.",
    (grids.GridTile, 'is_terrain_following'):
        "Set to true if the vertical coordinate system is terrain-following even if, as is often the case, this only applies to the lower levels of the grid.",
    (grids.GridTile, 'coord_file'):
        "This property may be used to specify the URI of a file containing grid coordinates that define the geometry of a a grid tile. It is envisaged that this will be the preferred mechanism for specifying the geometry of complex grids.",
    (grids.GridTile, 'is_uniform'):
        "If true, indicates that horizontal coordinates have fixed offsets in the X and Y directions. If the offset is the same in both directions then the grids are logically square, otherwise they are logically rectangular. The offsets can be specified by two scalar values (or three values in the case of 3D grids).",
    (grids.GridTile, 'coordinate_pole'):
        "gml:PointType:The coordinatePole property may be used to specify the lat-long position of any coordinate poles (in the mathematical sense) that form part of the definition of a grid tile. Not to be confused with the gridNorthPole property.  If required, two or more coordinate pole definitions may be distinguished by setting the gml:id attribute to appropriate values, such as spole, npole, etc.",
    (grids.GridTile, 'long_name'):
        None,
    (grids.GridTile, 'horizontal_crs'):
        "gml:CRSPropertyType:Specifies the horizontal coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external horizontal CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document.",
    (grids.GridTile, 'vertical_crs'):
        "gml:CRSPropertyType:Specifies the vertical coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external vertical CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document.",
    (grids.GridTile, 'mnemonic'):
        None,
    (grids.GridTile, 'grid_north_pole'):
        "gml:PointType:If required, defines the lat-long position of the north pole used by the grid tile in the case of rotated/displaced pole grids. Not to be confused with the coordinatePole property.",
    (grids.GridTile, 'nx'):
        "Specifies the length of the X, or longitude, dimension of the grid tile.",
    (grids.GridTile, 'simple_grid_geom'):
        "SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type.",
    (grids.GridTile, 'ny'):
        "Specifies the length of the Y, or latitude, dimension of the grid tile.",
    (grids.GridTile, 'nz'):
        "Specifies the length of the Z, or height/level, dimension of the grid tile. The zcoords coordinate list property, if specified, should have this length.",
    (grids.GridTile, 'description'):
        "A free-text description of a grid tile.",
    (grids.GridTile, 'discretization_type'):
        "Indicates the type of discretization applied to the grid tile, e.g. 'logically_rectangular'.",
    (grids.GridTile, 'short_name'):
        None,
    (grids.GridTile, 'refinement_scheme'):
        None,
    (grids.GridTile, 'extent'):
        None,
    (grids.GridTile, 'vertical_resolution'):
        "Provides an indication of the approximate resolution of the grid tile in the vertical dimension. (Added to align with corresponding ESG/Curator and DIF property).",
    (grids.GridMosaic, 'short_name'):
        "Specifies the short name associated with a grid mosaic. The short name will typically be a convenient abbreviation used to refer to a grid mosaic, e.g. 'UM ATM N96'.",
    (grids.GridMosaic, 'id'):
        "Specifies a globally unique identifier for a grid mosaic instance. By globally we mean across all GridSpec instances/records within a given modelling activity (such as CMIP5).",
    (grids.GridMosaic, 'mnemonic'):
        None,
    (grids.GridMosaic, 'mosaics'):
        None,
    (grids.GridMosaic, 'type'):
        "Specifies the type of all the grid tiles contained in a grid mosaic. It is assumed that all of the tiles comprising a given grid mosaic are of the same type. The value domain is as per the specified enumeration list.",
    (grids.GridMosaic, 'is_leaf'):
        "Indicates whether or not a grid mosaic is a leaf mosaic, that is, it only contains child grid tiles not further mosaics.",
    (grids.GridMosaic, 'description'):
        "A free-text description of a grid mosaic.",
    (grids.GridMosaic, 'tile_count'):
        "Specifies the number of tiles associated with a leaf grid mosaic. Set to zero if the grid mosaic is not a leaf mosaic, i.e. it contains child grid mosaics rather than tiles. (Added to align with equivalent ESG/Curator property.)",
    (grids.GridMosaic, 'extent'):
        None,
    (grids.GridMosaic, 'long_name'):
        "Specifies the long name associated with a grid mosaic. The long name will typically be a human-readable string, with acronyms expanded, used for labelling purposes.",
    (grids.GridMosaic, 'mosaic_count'):
        "Specifies the number of mosaics associated with a non-leaf grid mosaic. Set to zero if the grid mosaic is a leaf mosaic, i.e. it contains child grid tiles not mosaics.",
    (grids.GridMosaic, 'tiles'):
        None,
    (grids.GridMosaic, 'has_congruent_tiles'):
        "Indicates whether or not all the tiles contained within a grid mosaic are congruent, that is, of the same size and shape.",
    (grids.GridMosaic, 'citations'):
        "Optional container element for specifying a list of references that describe the grid.",
    (grids.VerticalCoordinateList, 'form'):
        "Units of measure used by the coordinates.",
    (grids.VerticalCoordinateList, 'type'):
        "Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used.",
    (grids.VerticalCoordinateList, 'properties'):
        None,
    (quality.Measure, 'description'):
        None,
    (quality.Measure, 'name'):
        None,
    (quality.Measure, 'identification'):
        None,
    (quality.Report, 'evaluator'):
        None,
    (quality.Report, 'date'):
        None,
    (quality.Report, 'measure'):
        None,
    (quality.Report, 'evaluation'):
        None,
    (quality.CimQuality, 'meta'):
        None,
    (quality.CimQuality, 'reports'):
        None,
    (quality.Evaluation, 'date'):
        None,
    (quality.Evaluation, 'type'):
        None,
    (quality.Evaluation, 'specification'):
        None,
    (quality.Evaluation, 'specification_hyperlink'):
        None,
    (quality.Evaluation, 'title'):
        None,
    (quality.Evaluation, 'did_pass'):
        None,
    (quality.Evaluation, 'type_hyperlink'):
        None,
    (quality.Evaluation, 'description'):
        None,
    (quality.Evaluation, 'explanation'):
        None,
    (misc.DocumentSet, 'data'):
        "Associated input/output data.",
    (misc.DocumentSet, 'grids'):
        "Associated grid-spec.",
    (misc.DocumentSet, 'model'):
        "Associated model component.",
    (misc.DocumentSet, 'meta'):
        None,
    (misc.DocumentSet, 'platform'):
        "Associated simulation execution platform.",
    (misc.DocumentSet, 'ensembles'):
        "Associated ensemble runs.",
    (misc.DocumentSet, 'simulation'):
        "Associated simulation run.",
    (misc.DocumentSet, 'experiment'):
        "Associated numerical experiment.",
    (activity.Experiment, 'measurement_campaigns'):
        None,
    (activity.Experiment, 'supports'):
        None,
    (activity.Experiment, 'generates'):
        None,
    (activity.Experiment, 'requires'):
        None,
    (activity.SimulationRelationship, 'target'):
        None,
    (activity.SimulationRelationship, 'type'):
        None,
    (activity.DownscalingSimulation, 'downscaling_type'):
        None,
    (activity.DownscalingSimulation, 'meta'):
        None,
    (activity.DownscalingSimulation, 'outputs'):
        None,
    (activity.DownscalingSimulation, 'downscaling_id'):
        None,
    (activity.DownscalingSimulation, 'downscaled_from'):
        None,
    (activity.DownscalingSimulation, 'calendar'):
        None,
    (activity.DownscalingSimulation, 'inputs'):
        "Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.",
    (activity.NumericalRequirement, 'options'):
        None,
    (activity.NumericalRequirement, 'id'):
        None,
    (activity.NumericalRequirement, 'description'):
        None,
    (activity.NumericalRequirement, 'source'):
        None,
    (activity.NumericalRequirement, 'requirement_type'):
        "Type of reqirement to which the experiment must conform.",
    (activity.NumericalRequirement, 'name'):
        None,
    (activity.EnsembleMember, 'simulation'):
        None,
    (activity.EnsembleMember, 'ensemble'):
        None,
    (activity.EnsembleMember, 'ensemble_ids'):
        None,
    (activity.NumericalActivity, 'supports'):
        None,
    (activity.NumericalActivity, 'description'):
        "A free-text description of the experiment.",
    (activity.NumericalActivity, 'short_name'):
        "The name of the experiment (that is used internally).",
    (activity.NumericalActivity, 'long_name'):
        "The name of the experiment (that is recognized externally).",
    (activity.Simulation, 'restarts'):
        None,
    (activity.Simulation, 'inputs'):
        "Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.",
    (activity.Simulation, 'spinup_date_range'):
        "The date range that a simulation is engaged in spinup.",
    (activity.Simulation, 'control_simulation'):
        "Points to a simulation being used as the basis (control) run.  Note that only 'derived' simulations can describe something as being control; a simulation should not know if it is being used itself as the control of some other run.",
    (activity.Simulation, 'authors'):
        "List of associated authors.",
    (activity.Simulation, 'spinup_simulation'):
        "The (external) simulation used during 'spinup.'  Note that this element can be used in conjuntion with spinupDateRange.  If a simulation has the latter but not the former, then one can assume that the simulation is performing its own spinup.",
    (activity.Simulation, 'simulation_id'):
        None,
    (activity.Simulation, 'outputs'):
        None,
    (activity.Simulation, 'conformances'):
        None,
    (activity.Simulation, 'deployments'):
        None,
    (activity.Simulation, 'calendar'):
        None,
    (activity.ExperimentRelationship, 'target'):
        None,
    (activity.ExperimentRelationship, 'type'):
        None,
    (activity.ExperimentRelationshipTarget, 'numerical_experiment'):
        None,
    (activity.NumericalRequirementOption, 'sub_options'):
        None,
    (activity.NumericalRequirementOption, 'name'):
        None,
    (activity.NumericalRequirementOption, 'relationship'):
        "Describes how this optional (child) requirement is related to its sibling requirements.  For example, a NumericalRequirement could consist of a set of optional requirements each with an 'OR' relationship meaning use this boundary condition _or_ that one.",
    (activity.NumericalRequirementOption, 'description'):
        None,
    (activity.NumericalRequirementOption, 'id'):
        None,
    (activity.Activity, 'responsible_parties'):
        "The point of contact(s) for this activity.This includes, among others, the principle investigator.",
    (activity.Activity, 'funding_sources'):
        "The entities that funded this activity.",
    (activity.Activity, 'rationales'):
        "For what purpose is this activity being performed?",
    (activity.Activity, 'projects'):
        "The project(s) that this activity is associated with (ie: CMIP5, AMIP, etc).",
    (activity.SimulationRelationshipTarget, 'simulation'):
        None,
    (activity.SimulationRelationshipTarget, 'target'):
        None,
    (activity.SpatioTemporalConstraint, 'date_range'):
        None,
    (activity.SpatioTemporalConstraint, 'spatial_resolution'):
        None,
    (activity.MeasurementCampaign, 'duration'):
        None,
    (activity.Conformance, 'description'):
        None,
    (activity.Conformance, 'sources'):
        "Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.",
    (activity.Conformance, 'frequency'):
        None,
    (activity.Conformance, 'type'):
        "Describes the method that this simulation conforms to an experimental requirement (in case it is not specified by the change property of the reference to the source of this conformance)",
    (activity.Conformance, 'is_conformant'):
        "Records whether or not this conformance satisfies the requirement.  A simulation should have at least one conformance mapping to every experimental requirement.  If a simulation satisfies the requirement - the usual case - then conformant should have a value of true.  If conformant is true but there is no reference to a source for the conformance, then we can assume that the simulation conforms to the requirement _naturally_, that is without having to modify code or inputs. If a simulation does not conform to a requirement then conformant should be set to false.",
    (activity.Conformance, 'requirements'):
        "Points to the NumericalRequirement that the simulation in question is conforming to.",
    (activity.Ensemble, 'outputs'):
        "Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.",
    (activity.Ensemble, 'members'):
        None,
    (activity.Ensemble, 'types'):
        None,
    (activity.Ensemble, 'meta'):
        None,
    (activity.SimulationRun, 'model'):
        None,
    (activity.SimulationRun, 'date_range'):
        None,
    (activity.SimulationRun, 'meta'):
        None,
    (activity.SimulationComposite, 'meta'):
        None,
    (activity.SimulationComposite, 'rank'):
        "Position of a simulation in the SimulationComposite timeline. eg:  Is this the first (rank = 1) or second (rank = 2) simulation",
    (activity.SimulationComposite, 'child'):
        None,
    (activity.SimulationComposite, 'date_range'):
        None,
    (activity.NumericalExperiment, 'requirements'):
        "The name of the experiment (that is used internally).",
    (activity.NumericalExperiment, 'meta'):
        None,
    (activity.NumericalExperiment, 'description'):
        "A free-text description of the experiment.",
    (activity.NumericalExperiment, 'short_name'):
        "The name of the experiment (that is used internally).",
    (activity.NumericalExperiment, 'experiment_id'):
        "An experiment ID takes the form <number>.<number>[-<letter>].",
    (activity.NumericalExperiment, 'long_name'):
        "The name of the experiment (that is recognized externally).",
    (software.Coupling, 'target'):
        "The target component of the coupling.",
    (software.Coupling, 'priming'):
        "A priming source is one that is active on the first available timestep only (before 'proper' coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.",
    (software.Coupling, 'time_lag'):
        "The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.",
    (software.Coupling, 'type'):
        "Describes the method of coupling.",
    (software.Coupling, 'sources'):
        "The source component of the coupling. (note that there can be multiple sources).",
    (software.Coupling, 'connections'):
        None,
    (software.Coupling, 'spatial_regriddings'):
        "Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).",
    (software.Coupling, 'description'):
        "A free-text description of the coupling.",
    (software.Coupling, 'properties'):
        None,
    (software.Coupling, 'time_transformation'):
        "Temporal transformation performed on the coupling field before or after regridding onto the target grid.",
    (software.Coupling, 'transformers'):
        "An 'in-line' transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.",
    (software.Coupling, 'purpose'):
        None,
    (software.Coupling, 'time_profile'):
        "Describes how often the coupling takes place.",
    (software.Coupling, 'is_fully_specified'):
        "If true then the coupling is fully-specified.  If false then not every Connection has been described within the coupling.",
    (software.Parallelisation, 'processes'):
        None,
    (software.Parallelisation, 'ranks'):
        None,
    (software.SpatialRegridding, 'user_method'):
        None,
    (software.SpatialRegridding, 'standard_method'):
        None,
    (software.SpatialRegridding, 'dimension'):
        None,
    (software.SpatialRegridding, 'properties'):
        None,
    (software.EntryPoint, 'name'):
        None,
    (software.ProcessorComponent, 'meta'):
        None,
    (software.StatisticalModelComponent, 'meta'):
        None,
    (software.StatisticalModelComponent, 'types'):
        "Describes the type of component. There can be multiple types.",
    (software.StatisticalModelComponent, 'type'):
        "Describes the type of component. There can be multiple types.",
    (software.StatisticalModelComponent, 'timing'):
        "Describes information about how this component simulates time.",
    (software.Composition, 'couplings'):
        None,
    (software.Composition, 'description'):
        None,
    (software.Timing, 'start'):
        None,
    (software.Timing, 'units'):
        None,
    (software.Timing, 'end'):
        None,
    (software.Timing, 'rate'):
        None,
    (software.Timing, 'is_variable_rate'):
        "Describes whether or not the model supports a variable timestep. If set to true, then rate should not be specified.",
    (software.ComponentLanguage, 'name'):
        "The name of the language.",
    (software.ComponentLanguage, 'properties'):
        None,
    (software.SpatialRegriddingUserMethod, 'file'):
        None,
    (software.SpatialRegriddingUserMethod, 'name'):
        None,
    (software.ComponentProperty, 'values'):
        "The value of the property (not applicable to fields).",
    (software.ComponentProperty, 'grid'):
        "A reference to the grid that is used by this component.",
    (software.ComponentProperty, 'sub_properties'):
        None,
    (software.ComponentProperty, 'standard_names'):
        None,
    (software.ComponentProperty, 'intent'):
        "The direction that this property is intended to be coupled: in, out, or inout.",
    (software.ComponentProperty, 'description'):
        None,
    (software.ComponentProperty, 'units'):
        "The standard name that this property is known as (for example, its CF name).",
    (software.ComponentProperty, 'citations'):
        None,
    (software.ComponentProperty, 'short_name'):
        None,
    (software.ComponentProperty, 'long_name'):
        None,
    (software.ComponentProperty, 'is_represented'):
        "When set to false, means that this property is not used by the component. Covers the case when, for instance, a modeler chooses not to represent some property in their model. (But still allows meaningful comparisons between components which _do_ model this property.)",
    (software.TimeTransformation, 'description'):
        None,
    (software.TimeTransformation, 'mapping_type'):
        None,
    (software.Deployment, 'parallelisation'):
        None,
    (software.Deployment, 'platform'):
        "The platform that this deployment has been run on. It is optional to allow for 'unconfigured' models, that nonetheless specify their parallelisation constraints (a feature needed by OASIS).",
    (software.Deployment, 'description'):
        None,
    (software.Deployment, 'executable_name'):
        None,
    (software.Deployment, 'executable_arguments'):
        None,
    (software.Deployment, 'deployment_date'):
        None,
    (software.Component, 'dependencies'):
        None,
    (software.Component, 'version'):
        "A free text description of the component version #.",
    (software.Component, 'deployments'):
        None,
    (software.Component, 'description'):
        "A free-text description of the component.",
    (software.Component, 'funding_sources'):
        "The entities that funded this software component.",
    (software.Component, 'grid'):
        "A reference to the grid that is used by this component.",
    (software.Component, 'is_embedded'):
        "An embedded component cannot exist on its own as an atomic piece of software; instead it is embedded within another (parent) component. When embedded equals 'true', the SoftwareComponent has a corresponding piece of software (otherwise it is acting as a 'virtual' component which may be inexorably nested within a piece of software along with several other virtual components).",
    (software.Component, 'language'):
        None,
    (software.Component, 'license'):
        "The license held by this piece of software.",
    (software.Component, 'long_name'):
        "The name of the model (that is recognized externally).",
    (software.Component, 'online_resource'):
        "Provides a URL location for this model.",
    (software.Component, 'parent'):
        None,
    (software.Component, 'sub_components'):
        None,
    (software.Component, 'previous_version'):
        None,
    (software.Component, 'citations'):
        None,
    (software.Component, 'properties'):
        "The properties that this model simulates and/or couples.",
    (software.Component, 'code_access'):
        "Instructions on how to access the source code for this component.",
    (software.Component, 'release_date'):
        "The date of publication of the software component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)",
    (software.Component, 'composition'):
        None,
    (software.Component, 'responsible_parties'):
        None,
    (software.Component, 'coupling_framework'):
        "The coupling framework that this entire component conforms to.",
    (software.Component, 'short_name'):
        "The name of the model (that is used internally).",
    (software.ModelComponent, 'activity'):
        None,
    (software.ModelComponent, 'type'):
        "Describes the type of component. There can be multiple types.",
    (software.ModelComponent, 'meta'):
        None,
    (software.ModelComponent, 'types'):
        "Describes the type of component. There can be multiple types.",
    (software.ModelComponent, 'timing'):
        "Describes information about how this component simulates time.",
    (software.Rank, 'increment'):
        None,
    (software.Rank, 'min'):
        None,
    (software.Rank, 'value'):
        None,
    (software.Rank, 'max'):
        None,
    (software.CouplingEndpoint, 'properties'):
        "A place to describe features specific to the source/target of a coupling",
    (software.CouplingEndpoint, 'data_source'):
        None,
    (software.CouplingEndpoint, 'instance_id'):
        "If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).",
    (software.TimeLag, 'units'):
        None,
    (software.TimeLag, 'value'):
        None,
    (software.Connection, 'target'):
        "The target property being connected.  This is optional to support the way that input is handled in the CMIP5 questionnaire.",
    (software.Connection, 'transformers'):
        "An 'in-line' transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.",
    (software.Connection, 'priming'):
        "A priming source is one that is active on the first available timestep only (before 'proper' coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.",
    (software.Connection, 'description'):
        None,
    (software.Connection, 'time_profile'):
        "All information having to do with the rate of this connection; the times that it is active.  This overrides any rate of a Coupling.",
    (software.Connection, 'properties'):
        None,
    (software.Connection, 'time_transformation'):
        "Temporal transformation performed on the coupling field before or after regridding onto the target grid.",
    (software.Connection, 'sources'):
        "The source property being connected.  (note that there can be multiple sources)  This is optional; the file/component source may have already been specified by the couplingSource.",
    (software.Connection, 'spatial_regridding'):
        "Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)",
    (software.Connection, 'type'):
        "The type of Connection",
    (software.Connection, 'time_lag'):
        "The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.",
    (software.ConnectionEndpoint, 'properties'):
        "The place to describe features specific to the source/target of a connection.",
    (software.ConnectionEndpoint, 'data_source'):
        None,
    (software.ConnectionEndpoint, 'instance_id'):
        "If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).",

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    shared.InterconnectType: """
        A list of connectors between machines.

    """,
    shared.OperatingSystemType: """
        A list of common operating systems.

    """,
    shared.DocRelationshipDirectionType: """
        Creates and returns instance of relationship_direction_type enum.

    """,
    shared.DataPurpose: """
        Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.

    """,
    shared.DocStatusType: """
        Status of cim document.

    """,
    shared.UnitType: """
        A list of scientific units.

    """,
    shared.CompilerType: """
        Creates and returns instance of compiler_type enum.

    """,
    shared.DocRelationshipType: """
        Creates and returns instance of document_relationship_type enum.

    """,
    shared.MachineVendorType: """
        A list of organisations that create machines.

    """,
    shared.DocType: """
        Creates and returns instance of doc_type enum.

    """,
    shared.ChangePropertyType: """
        Creates and returns instance of change_property_type enum.

    """,
    shared.ProcessorType: """
        A list of known cpu's.

    """,
    shared.MachineType: """
        A list of known machines.

    """,
    data.DataHierarchyType: """
        Enumerates the level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.

    """,
    data.DataStatusType: """
        Enumerates status of a data object.

    """,
    grids.DiscretizationEnum: """
        Creates and returns instance of discretization_enum enum.

    """,
    grids.HorizontalCsEnum: """
        Creates and returns instance of horizontal_cs_enum enum.

    """,
    grids.ArcTypeEnum: """
        Creates and returns instance of arc_type_enum enum.

    """,
    grids.VerticalCsEnum: """
        Creates and returns instance of vertical_cs_enum enum.

    """,
    grids.RefinementTypeEnum: """
        Creates and returns instance of refinement_type_enum enum.

    """,
    grids.GridNodePositionEnum: """
        Creates and returns instance of grid_node_position_enum enum.

    """,
    grids.GridTypeEnum: """
        Creates and returns instance of grid_type_enum enum.

    """,
    grids.FeatureTypeEnum: """
        Creates and returns instance of feature_type_enum enum.

    """,
    grids.GeometryTypeEnum: """
        Creates and returns instance of geometry_type_enum enum.

    """,
    quality.CimFeatureType: """
        Creates and returns instance of cim_feature_type enum.

    """,
    quality.CimScopeCodeType: """
        This would cover quality issues with the CIM itself.

    """,
    quality.QualityStatusType: """
        Creates and returns instance of quality_status_type enum.

    """,
    quality.CimResultType: """
        Creates and returns instance of cim_result_type enum.

    """,
    quality.QualitySeverityType: """
        Creates and returns instance of quality_severity_type enum.

    """,
    quality.QualityIssueType: """
        Creates and returns instance of quality_issue_type enum.

    """,
    activity.EnsembleType: """
        Creates and returns instance of ensemble_type enum.

    """,
    activity.ExperimentRelationshipType: """
        Creates and returns instance of experiment_relationship_type enum.

    """,
    activity.DownscalingType: """
        Creates and returns instance of downscaling_type enum.

    """,
    activity.FrequencyType: """
        Creates and returns instance of frequency_type enum.

    """,
    activity.ProjectType: """
        Creates and returns instance of project_type enum.

    """,
    activity.ResolutionType: """
        Creates and returns instance of resolution_type enum.

    """,
    activity.SimulationType: """
        Creates and returns instance of simulation_type enum.

    """,
    activity.ConformanceType: """
        Creates and returns instance of conformance_type enum.

    """,
    activity.SimulationRelationshipType: """
        Creates and returns instance of simulation_relationship_type enum.

    """,
    software.ModelComponentType: """
        An enumeration of types of ModelComponent. This includes things like atmosphere & ocean models, radiation schemes, etc. CIM best-practice is to describe every component for which there is a named ComponentType as a separate component, even if it is not a separate unit of software (ie: even if it is embedded), instead of as a (set of) ModelParameters. This codelist is synonomous with 'realm' for the purposes of CMIP5.

    """,
    software.StatisticalModelComponentType: """
        An enumeration of types of ProcessorComponent.  This includes things like transformers and post-processors.

    """,
    software.SpatialRegriddingDimensionType: """
        Creates and returns instance of spatial_regridding_dimension_type enum.

    """,
    software.CouplingFrameworkType: """
        Creates and returns instance of coupling_framework_type enum.

    """,
    software.SpatialRegriddingStandardMethodType: """
        Creates and returns instance of spatial_regridding_standard_method_type enum.

    """,
    software.TimeMappingType: """
        Enumerates the different ways that time can be mapped when transforming from one field to another.

    """,
    software.ConnectionType: """
        The ConnectionType enumeration describes the mechanism of transport for a connection.

    """,
    software.TimingUnits: """
        Creates and returns instance of timing_units enum.

    """,
    software.ComponentPropertyIntentType: """
        The direction that the associated component property is intended to be coupled: in, out, or inout.

    """,

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (shared.DocRelationshipDirectionType, 'toTarget'):
        None,
    (shared.DocRelationshipDirectionType, 'fromTarget'):
        None,
    (shared.DataPurpose, 'boundaryCondition'):
        None,
    (shared.DataPurpose, 'ancillaryFile'):
        None,
    (shared.DataPurpose, 'initialCondition'):
        None,
    (shared.DocStatusType, 'incomplete'):
        None,
    (shared.DocStatusType, 'complete'):
        None,
    (shared.DocStatusType, 'in-progress'):
        None,
    (shared.DocRelationshipType, 'other'):
        None,
    (shared.DocRelationshipType, 'similarTo'):
        None,
    (shared.DocRelationshipType, 'previousVersionOf'):
        None,
    (shared.DocRelationshipType, 'fixedVersionOf'):
        None,
    (shared.DocRelationshipType, 'laterVersionOf'):
        None,
    (shared.DocType, 'dataObject'):
        None,
    (shared.DocType, 'simulationComposite'):
        None,
    (shared.DocType, 'gridSpec'):
        None,
    (shared.DocType, 'processorComponent'):
        None,
    (shared.DocType, 'cimQuality'):
        None,
    (shared.DocType, 'assimilation'):
        None,
    (shared.DocType, 'downscalingSimulation'):
        None,
    (shared.DocType, 'platform'):
        None,
    (shared.DocType, 'modelComponent'):
        None,
    (shared.DocType, 'simulationRun'):
        None,
    (shared.DocType, 'dataProcessing'):
        None,
    (shared.DocType, 'statisticalModelComponent'):
        None,
    (shared.DocType, 'ensemble'):
        None,
    (shared.DocType, 'numericalExperiment'):
        None,
    (shared.ChangePropertyType, 'BoundaryCondition'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'InitialCondition'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'ModelMod'):
        None,
    (shared.ChangePropertyType, 'Increment'):
        None,
    (shared.ChangePropertyType, 'Redistribution'):
        None,
    (shared.ChangePropertyType, 'InputMod'):
        None,
    (shared.ChangePropertyType, 'Replacement'):
        None,
    (shared.ChangePropertyType, 'ParameterChange'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'Unused'):
        None,
    (shared.ChangePropertyType, 'CodeChange'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'AncillaryFile'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'Decrement'):
        None,
    (shared.MachineType, 'Beowulf'):
        None,
    (shared.MachineType, 'Vector'):
        None,
    (shared.MachineType, 'Parallel'):
        None,
    (data.DataStatusType, 'complete'):
        "This DataObject is complete.",
    (data.DataStatusType, 'metadataOnly'):
        "This DataObject is incomplete - it is described in metadata but the actual data has not yet been linked to it.",
    (data.DataStatusType, 'continuouslySupplemented'):
        "This DataObject's actual data is continuously updated.",
    (grids.DiscretizationEnum, 'structured_triangular'):
        None,
    (grids.DiscretizationEnum, 'unstructured_triangular'):
        None,
    (grids.DiscretizationEnum, 'pixel-based_catchment'):
        None,
    (grids.DiscretizationEnum, 'unstructured_polygonal'):
        None,
    (grids.DiscretizationEnum, 'spherical_harmonics'):
        None,
    (grids.DiscretizationEnum, 'other'):
        None,
    (grids.DiscretizationEnum, 'logically_rectangular'):
        None,
    (grids.HorizontalCsEnum, 'spherical'):
        None,
    (grids.HorizontalCsEnum, 'cartesian'):
        None,
    (grids.HorizontalCsEnum, 'ellipsoidal'):
        None,
    (grids.HorizontalCsEnum, 'polar'):
        None,
    (grids.ArcTypeEnum, 'complex'):
        None,
    (grids.ArcTypeEnum, 'geodesic'):
        None,
    (grids.ArcTypeEnum, 'small_circle'):
        None,
    (grids.ArcTypeEnum, 'great_circle'):
        None,
    (grids.VerticalCsEnum, 'mass-based'):
        None,
    (grids.VerticalCsEnum, 'space-based'):
        None,
    (grids.RefinementTypeEnum, 'none'):
        "Tile boundaries have no refinement when the grid lines meeting at the tile boundary are continuous.",
    (grids.RefinementTypeEnum, 'integer'):
        "The refinement is integer when grid lines from the coarser grid are continuous on the finer grid, but not vice versa.",
    (grids.RefinementTypeEnum, 'rational'):
        "The refinement is rational when the adjacent or overlapping grid tiles have grid line counts that are coprime (i.e. no common factor other than 1).",
    (grids.GridNodePositionEnum, 'plane'):
        None,
    (grids.GridNodePositionEnum, 'centre'):
        None,
    (grids.GridNodePositionEnum, 'sphere'):
        None,
    (grids.GridTypeEnum, 'displaced_pole'):
        None,
    (grids.GridTypeEnum, 'icosahedral_geodesic'):
        None,
    (grids.GridTypeEnum, 'reduced_gaussian'):
        None,
    (grids.GridTypeEnum, 'regular_lat_lon'):
        None,
    (grids.GridTypeEnum, 'cubed_sphere'):
        None,
    (grids.GridTypeEnum, 'spectral_gaussian'):
        None,
    (grids.GridTypeEnum, 'tripolar'):
        None,
    (grids.GridTypeEnum, 'yin_yang'):
        None,
    (grids.GridTypeEnum, 'composite'):
        None,
    (grids.GridTypeEnum, 'other'):
        None,
    (grids.FeatureTypeEnum, 'edge'):
        None,
    (grids.FeatureTypeEnum, 'point'):
        None,
    (grids.GeometryTypeEnum, 'plane'):
        None,
    (grids.GeometryTypeEnum, 'ellipsoid'):
        None,
    (grids.GeometryTypeEnum, 'sphere'):
        None,
    (quality.CimFeatureType, 'diagnostic'):
        None,
    (quality.CimFeatureType, 'file'):
        None,
    (quality.CimScopeCodeType, 'model'):
        None,
    (quality.CimScopeCodeType, 'modelComponent'):
        None,
    (quality.CimScopeCodeType, 'simulation'):
        None,
    (quality.CimScopeCodeType, 'experiment'):
        None,
    (quality.CimScopeCodeType, 'numericalRequirement'):
        None,
    (quality.CimScopeCodeType, 'dataset'):
        None,
    (quality.CimScopeCodeType, 'software'):
        None,
    (quality.CimScopeCodeType, 'file'):
        None,
    (quality.CimScopeCodeType, 'service'):
        None,
    (quality.CimScopeCodeType, 'ensemble'):
        None,
    (quality.QualityStatusType, 'partially_resolved'):
        None,
    (quality.QualityStatusType, 'resolved'):
        None,
    (quality.QualityStatusType, 'confirmed'):
        None,
    (quality.QualityStatusType, 'reported'):
        None,
    (quality.CimResultType, 'document'):
        None,
    (quality.CimResultType, 'logfile'):
        None,
    (quality.CimResultType, 'plot'):
        None,
    (quality.QualitySeverityType, 'minor'):
        None,
    (quality.QualitySeverityType, 'cosmetic'):
        None,
    (quality.QualitySeverityType, 'major'):
        None,
    (quality.QualityIssueType, 'metadata'):
        None,
    (quality.QualityIssueType, 'data_content'):
        None,
    (quality.QualityIssueType, 'science'):
        None,
    (quality.QualityIssueType, 'data_format'):
        None,
    (quality.QualityIssueType, 'data_indexing'):
        None,
    (activity.ExperimentRelationshipType, 'modifiedInputMethodOf'):
        None,
    (activity.ExperimentRelationshipType, 'shorterVersionOf'):
        None,
    (activity.ExperimentRelationshipType, 'extensionOf'):
        None,
    (activity.ExperimentRelationshipType, 'continuationOf'):
        None,
    (activity.ExperimentRelationshipType, 'controlExperiment'):
        None,
    (activity.ExperimentRelationshipType, 'higherResolutionVersionOf'):
        None,
    (activity.ExperimentRelationshipType, 'previousRealisation'):
        None,
    (activity.ExperimentRelationshipType, 'lowerResolutionVersionOf'):
        None,
    (activity.ExperimentRelationshipType, 'increaseEnsembleOf'):
        None,
    (activity.DownscalingType, 'dynamic'):
        None,
    (activity.DownscalingType, 'statistical'):
        None,
    (activity.SimulationType, 'assimilation'):
        None,
    (activity.SimulationType, 'simulationComposite'):
        None,
    (activity.SimulationType, 'simulationRun'):
        None,
    (activity.ConformanceType, 'not conformant'):
        "Describes a simulation that is purpefully non-conformant to an experimental requirement.",
    (activity.ConformanceType, 'standard config'):
        "Describes a simulation that is 'naturally' conformant to an experimental requirement.",
    (activity.ConformanceType, 'via inputs'):
        "Describes a simulation that conforms to an experimental requirement by using particular inputs.",
    (activity.ConformanceType, 'via model mods'):
        "Describes a simulation that conforms to an experimental requirement by changing the configuration of the software model implementing that simulation.",
    (activity.ConformanceType, 'combination'):
        "Describes a simulation that conforms to an experimental requirement by using more than one method.",
    (activity.ConformanceType, 'not-xxx'):
        None,
    (activity.SimulationRelationshipType, 'continuationOf'):
        None,
    (activity.SimulationRelationshipType, 'previousSimulation'):
        None,
    (activity.SimulationRelationshipType, 'higherResolutionVersionOf'):
        None,
    (activity.SimulationRelationshipType, 'lowerResolutionVersionOf'):
        None,
    (activity.SimulationRelationshipType, 'fixedVersionOf'):
        None,
    (activity.SimulationRelationshipType, 'followingSimulation'):
        None,
    (activity.SimulationRelationshipType, 'extensionOf'):
        None,
    (activity.SimulationRelationshipType, 'responseTo'):
        None,
    (software.SpatialRegriddingDimensionType, '1D'):
        None,
    (software.SpatialRegriddingDimensionType, '2D'):
        None,
    (software.SpatialRegriddingDimensionType, '3D'):
        None,
    (software.CouplingFrameworkType, 'ESMF'):
        None,
    (software.CouplingFrameworkType, 'BFG'):
        None,
    (software.CouplingFrameworkType, 'OASIS'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'cubic'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'conservative-first-order'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'conservative-second-order'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'conservative'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'non-conservative'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'linear'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'near-neighbour'):
        None,
    (software.TimingUnits, 'seconds'):
        None,
    (software.TimingUnits, 'minutes'):
        None,
    (software.TimingUnits, 'hours'):
        None,
    (software.TimingUnits, 'days'):
        None,
    (software.TimingUnits, 'months'):
        None,
    (software.TimingUnits, 'years'):
        None,
    (software.TimingUnits, 'decades'):
        None,
    (software.TimingUnits, 'centuries'):
        None,
    (software.ComponentPropertyIntentType, 'in'):
        None,
    (software.ComponentPropertyIntentType, 'out'):
        None,
    (software.ComponentPropertyIntentType, 'inout'):
        None,
}

# ------------------------------------------------
# Type keys.
# ------------------------------------------------

# Map of ontology types to type keys.
KEYS = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    shared: "cim.1.shared",
    data: "cim.1.data",
    grids: "cim.1.grids",
    quality: "cim.1.quality",
    misc: "cim.1.misc",
    activity: "cim.1.activity",
    software: "cim.1.software",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    shared.DocReference: "cim.1.shared.DocReference",
    shared.DateRange: "cim.1.shared.DateRange",
    shared.Change: "cim.1.shared.Change",
    shared.OpenDateRange: "cim.1.shared.OpenDateRange",
    shared.DocRelationship: "cim.1.shared.DocRelationship",
    shared.Daily360: "cim.1.shared.Daily360",
    shared.Standard: "cim.1.shared.Standard",
    shared.RealCalendar: "cim.1.shared.RealCalendar",
    shared.DocRelationshipTarget: "cim.1.shared.DocRelationshipTarget",
    shared.Citation: "cim.1.shared.Citation",
    shared.Property: "cim.1.shared.Property",
    shared.License: "cim.1.shared.License",
    shared.Machine: "cim.1.shared.Machine",
    shared.DataSource: "cim.1.shared.DataSource",
    shared.DocGenealogy: "cim.1.shared.DocGenealogy",
    shared.MachineCompilerUnit: "cim.1.shared.MachineCompilerUnit",
    shared.Relationship: "cim.1.shared.Relationship",
    shared.Compiler: "cim.1.shared.Compiler",
    shared.PerpetualPeriod: "cim.1.shared.PerpetualPeriod",
    shared.Platform: "cim.1.shared.Platform",
    shared.ClosedDateRange: "cim.1.shared.ClosedDateRange",
    shared.Calendar: "cim.1.shared.Calendar",
    shared.ResponsibleParty: "cim.1.shared.ResponsibleParty",
    shared.DocMetaInfo: "cim.1.shared.DocMetaInfo",
    shared.ChangeProperty: "cim.1.shared.ChangeProperty",
    shared.StandardName: "cim.1.shared.StandardName",
    data.DataDistribution: "cim.1.data.DataDistribution",
    data.DataProperty: "cim.1.data.DataProperty",
    data.DataStorageFile: "cim.1.data.DataStorageFile",
    data.DataExtentTemporal: "cim.1.data.DataExtentTemporal",
    data.DataExtentTimeInterval: "cim.1.data.DataExtentTimeInterval",
    data.DataRestriction: "cim.1.data.DataRestriction",
    data.DataStorage: "cim.1.data.DataStorage",
    data.DataExtentGeographical: "cim.1.data.DataExtentGeographical",
    data.DataObject: "cim.1.data.DataObject",
    data.DataHierarchyLevel: "cim.1.data.DataHierarchyLevel",
    data.DataExtent: "cim.1.data.DataExtent",
    data.DataContent: "cim.1.data.DataContent",
    data.DataTopic: "cim.1.data.DataTopic",
    data.DataStorageDb: "cim.1.data.DataStorageDb",
    data.DataStorageIp: "cim.1.data.DataStorageIp",
    grids.GridExtent: "cim.1.grids.GridExtent",
    grids.GridTileResolutionType: "cim.1.grids.GridTileResolutionType",
    grids.GridProperty: "cim.1.grids.GridProperty",
    grids.SimpleGridGeometry: "cim.1.grids.SimpleGridGeometry",
    grids.GridSpec: "cim.1.grids.GridSpec",
    grids.CoordinateList: "cim.1.grids.CoordinateList",
    grids.GridTile: "cim.1.grids.GridTile",
    grids.GridMosaic: "cim.1.grids.GridMosaic",
    grids.VerticalCoordinateList: "cim.1.grids.VerticalCoordinateList",
    quality.Measure: "cim.1.quality.Measure",
    quality.Report: "cim.1.quality.Report",
    quality.CimQuality: "cim.1.quality.CimQuality",
    quality.Evaluation: "cim.1.quality.Evaluation",
    misc.DocumentSet: "cim.1.misc.DocumentSet",
    activity.Experiment: "cim.1.activity.Experiment",
    activity.SimulationRelationship: "cim.1.activity.SimulationRelationship",
    activity.DownscalingSimulation: "cim.1.activity.DownscalingSimulation",
    activity.LateralBoundaryCondition: "cim.1.activity.LateralBoundaryCondition",
    activity.NumericalRequirement: "cim.1.activity.NumericalRequirement",
    activity.EnsembleMember: "cim.1.activity.EnsembleMember",
    activity.InitialCondition: "cim.1.activity.InitialCondition",
    activity.NumericalActivity: "cim.1.activity.NumericalActivity",
    activity.Simulation: "cim.1.activity.Simulation",
    activity.ExperimentRelationship: "cim.1.activity.ExperimentRelationship",
    activity.ExperimentRelationshipTarget: "cim.1.activity.ExperimentRelationshipTarget",
    activity.NumericalRequirementOption: "cim.1.activity.NumericalRequirementOption",
    activity.Activity: "cim.1.activity.Activity",
    activity.SimulationRelationshipTarget: "cim.1.activity.SimulationRelationshipTarget",
    activity.SpatioTemporalConstraint: "cim.1.activity.SpatioTemporalConstraint",
    activity.OutputRequirement: "cim.1.activity.OutputRequirement",
    activity.MeasurementCampaign: "cim.1.activity.MeasurementCampaign",
    activity.Conformance: "cim.1.activity.Conformance",
    activity.BoundaryCondition: "cim.1.activity.BoundaryCondition",
    activity.Ensemble: "cim.1.activity.Ensemble",
    activity.SimulationRun: "cim.1.activity.SimulationRun",
    activity.PhysicalModification: "cim.1.activity.PhysicalModification",
    activity.SimulationComposite: "cim.1.activity.SimulationComposite",
    activity.NumericalExperiment: "cim.1.activity.NumericalExperiment",
    software.Coupling: "cim.1.software.Coupling",
    software.Parallelisation: "cim.1.software.Parallelisation",
    software.SpatialRegridding: "cim.1.software.SpatialRegridding",
    software.EntryPoint: "cim.1.software.EntryPoint",
    software.ProcessorComponent: "cim.1.software.ProcessorComponent",
    software.ConnectionProperty: "cim.1.software.ConnectionProperty",
    software.StatisticalModelComponent: "cim.1.software.StatisticalModelComponent",
    software.Composition: "cim.1.software.Composition",
    software.Timing: "cim.1.software.Timing",
    software.ComponentLanguage: "cim.1.software.ComponentLanguage",
    software.SpatialRegriddingUserMethod: "cim.1.software.SpatialRegriddingUserMethod",
    software.ComponentLanguageProperty: "cim.1.software.ComponentLanguageProperty",
    software.SpatialRegriddingProperty: "cim.1.software.SpatialRegriddingProperty",
    software.ComponentProperty: "cim.1.software.ComponentProperty",
    software.TimeTransformation: "cim.1.software.TimeTransformation",
    software.Deployment: "cim.1.software.Deployment",
    software.Component: "cim.1.software.Component",
    software.ModelComponent: "cim.1.software.ModelComponent",
    software.Rank: "cim.1.software.Rank",
    software.CouplingEndpoint: "cim.1.software.CouplingEndpoint",
    software.TimeLag: "cim.1.software.TimeLag",
    software.Connection: "cim.1.software.Connection",
    software.ConnectionEndpoint: "cim.1.software.ConnectionEndpoint",
    software.CouplingProperty: "cim.1.software.CouplingProperty",

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (shared.DocReference, 'id'): "cim.1.shared.DocReference.id",
    (shared.DocReference, 'description'): "cim.1.shared.DocReference.description",
    (shared.DocReference, 'changes'): "cim.1.shared.DocReference.changes",
    (shared.DocReference, 'url'): "cim.1.shared.DocReference.url",
    (shared.DocReference, 'type'): "cim.1.shared.DocReference.type",
    (shared.DocReference, 'name'): "cim.1.shared.DocReference.name",
    (shared.DocReference, 'external_id'): "cim.1.shared.DocReference.external_id",
    (shared.DocReference, 'version'): "cim.1.shared.DocReference.version",
    (shared.DateRange, 'duration'): "cim.1.shared.DateRange.duration",
    (shared.Change, 'description'): "cim.1.shared.Change.description",
    (shared.Change, 'name'): "cim.1.shared.Change.name",
    (shared.Change, 'details'): "cim.1.shared.Change.details",
    (shared.Change, 'author'): "cim.1.shared.Change.author",
    (shared.Change, 'date'): "cim.1.shared.Change.date",
    (shared.Change, 'type'): "cim.1.shared.Change.type",
    (shared.OpenDateRange, 'end'): "cim.1.shared.OpenDateRange.end",
    (shared.OpenDateRange, 'start'): "cim.1.shared.OpenDateRange.start",
    (shared.DocRelationship, 'type'): "cim.1.shared.DocRelationship.type",
    (shared.DocRelationship, 'target'): "cim.1.shared.DocRelationship.target",
    (shared.Standard, 'version'): "cim.1.shared.Standard.version",
    (shared.Standard, 'description'): "cim.1.shared.Standard.description",
    (shared.Standard, 'name'): "cim.1.shared.Standard.name",
    (shared.DocRelationshipTarget, 'reference'): "cim.1.shared.DocRelationshipTarget.reference",
    (shared.Citation, 'alternative_title'): "cim.1.shared.Citation.alternative_title",
    (shared.Citation, 'date_type'): "cim.1.shared.Citation.date_type",
    (shared.Citation, 'collective_title'): "cim.1.shared.Citation.collective_title",
    (shared.Citation, 'organisation'): "cim.1.shared.Citation.organisation",
    (shared.Citation, 'location'): "cim.1.shared.Citation.location",
    (shared.Citation, 'role'): "cim.1.shared.Citation.role",
    (shared.Citation, 'date'): "cim.1.shared.Citation.date",
    (shared.Citation, 'title'): "cim.1.shared.Citation.title",
    (shared.Citation, 'type'): "cim.1.shared.Citation.type",
    (shared.Property, 'name'): "cim.1.shared.Property.name",
    (shared.Property, 'value'): "cim.1.shared.Property.value",
    (shared.License, 'contact'): "cim.1.shared.License.contact",
    (shared.License, 'name'): "cim.1.shared.License.name",
    (shared.License, 'is_unrestricted'): "cim.1.shared.License.is_unrestricted",
    (shared.License, 'description'): "cim.1.shared.License.description",
    (shared.Machine, 'libraries'): "cim.1.shared.Machine.libraries",
    (shared.Machine, 'system'): "cim.1.shared.Machine.system",
    (shared.Machine, 'cores_per_processor'): "cim.1.shared.Machine.cores_per_processor",
    (shared.Machine, 'location'): "cim.1.shared.Machine.location",
    (shared.Machine, 'type'): "cim.1.shared.Machine.type",
    (shared.Machine, 'operating_system'): "cim.1.shared.Machine.operating_system",
    (shared.Machine, 'maximum_processors'): "cim.1.shared.Machine.maximum_processors",
    (shared.Machine, 'vendor'): "cim.1.shared.Machine.vendor",
    (shared.Machine, 'description'): "cim.1.shared.Machine.description",
    (shared.Machine, 'name'): "cim.1.shared.Machine.name",
    (shared.Machine, 'processor_type'): "cim.1.shared.Machine.processor_type",
    (shared.Machine, 'interconnect'): "cim.1.shared.Machine.interconnect",
    (shared.DataSource, 'purpose'): "cim.1.shared.DataSource.purpose",
    (shared.DocGenealogy, 'relationships'): "cim.1.shared.DocGenealogy.relationships",
    (shared.MachineCompilerUnit, 'compilers'): "cim.1.shared.MachineCompilerUnit.compilers",
    (shared.MachineCompilerUnit, 'machine'): "cim.1.shared.MachineCompilerUnit.machine",
    (shared.Relationship, 'description'): "cim.1.shared.Relationship.description",
    (shared.Relationship, 'direction'): "cim.1.shared.Relationship.direction",
    (shared.Compiler, 'language'): "cim.1.shared.Compiler.language",
    (shared.Compiler, 'version'): "cim.1.shared.Compiler.version",
    (shared.Compiler, 'name'): "cim.1.shared.Compiler.name",
    (shared.Compiler, 'environment_variables'): "cim.1.shared.Compiler.environment_variables",
    (shared.Compiler, 'options'): "cim.1.shared.Compiler.options",
    (shared.Compiler, 'type'): "cim.1.shared.Compiler.type",
    (shared.Platform, 'meta'): "cim.1.shared.Platform.meta",
    (shared.Platform, 'units'): "cim.1.shared.Platform.units",
    (shared.Platform, 'contacts'): "cim.1.shared.Platform.contacts",
    (shared.Platform, 'description'): "cim.1.shared.Platform.description",
    (shared.Platform, 'long_name'): "cim.1.shared.Platform.long_name",
    (shared.Platform, 'short_name'): "cim.1.shared.Platform.short_name",
    (shared.ClosedDateRange, 'end'): "cim.1.shared.ClosedDateRange.end",
    (shared.ClosedDateRange, 'start'): "cim.1.shared.ClosedDateRange.start",
    (shared.Calendar, 'range'): "cim.1.shared.Calendar.range",
    (shared.Calendar, 'description'): "cim.1.shared.Calendar.description",
    (shared.Calendar, 'length'): "cim.1.shared.Calendar.length",
    (shared.ResponsibleParty, 'url'): "cim.1.shared.ResponsibleParty.url",
    (shared.ResponsibleParty, 'individual_name'): "cim.1.shared.ResponsibleParty.individual_name",
    (shared.ResponsibleParty, 'abbreviation'): "cim.1.shared.ResponsibleParty.abbreviation",
    (shared.ResponsibleParty, 'organisation_name'): "cim.1.shared.ResponsibleParty.organisation_name",
    (shared.ResponsibleParty, 'address'): "cim.1.shared.ResponsibleParty.address",
    (shared.ResponsibleParty, 'role'): "cim.1.shared.ResponsibleParty.role",
    (shared.ResponsibleParty, 'email'): "cim.1.shared.ResponsibleParty.email",
    (shared.DocMetaInfo, 'status'): "cim.1.shared.DocMetaInfo.status",
    (shared.DocMetaInfo, 'type_sort_key'): "cim.1.shared.DocMetaInfo.type_sort_key",
    (shared.DocMetaInfo, 'drs_path'): "cim.1.shared.DocMetaInfo.drs_path",
    (shared.DocMetaInfo, 'source'): "cim.1.shared.DocMetaInfo.source",
    (shared.DocMetaInfo, 'type_display_name'): "cim.1.shared.DocMetaInfo.type_display_name",
    (shared.DocMetaInfo, 'language'): "cim.1.shared.DocMetaInfo.language",
    (shared.DocMetaInfo, 'drs_keys'): "cim.1.shared.DocMetaInfo.drs_keys",
    (shared.DocMetaInfo, 'institute'): "cim.1.shared.DocMetaInfo.institute",
    (shared.DocMetaInfo, 'source_key'): "cim.1.shared.DocMetaInfo.source_key",
    (shared.DocMetaInfo, 'author'): "cim.1.shared.DocMetaInfo.author",
    (shared.DocMetaInfo, 'update_date'): "cim.1.shared.DocMetaInfo.update_date",
    (shared.DocMetaInfo, 'external_ids'): "cim.1.shared.DocMetaInfo.external_ids",
    (shared.DocMetaInfo, 'sort_key'): "cim.1.shared.DocMetaInfo.sort_key",
    (shared.DocMetaInfo, 'type'): "cim.1.shared.DocMetaInfo.type",
    (shared.DocMetaInfo, 'version'): "cim.1.shared.DocMetaInfo.version",
    (shared.DocMetaInfo, 'create_date'): "cim.1.shared.DocMetaInfo.create_date",
    (shared.DocMetaInfo, 'project'): "cim.1.shared.DocMetaInfo.project",
    (shared.DocMetaInfo, 'genealogy'): "cim.1.shared.DocMetaInfo.genealogy",
    (shared.DocMetaInfo, 'id'): "cim.1.shared.DocMetaInfo.id",
    (shared.ChangeProperty, 'description'): "cim.1.shared.ChangeProperty.description",
    (shared.ChangeProperty, 'id'): "cim.1.shared.ChangeProperty.id",
    (shared.StandardName, 'is_open'): "cim.1.shared.StandardName.is_open",
    (shared.StandardName, 'value'): "cim.1.shared.StandardName.value",
    (shared.StandardName, 'standards'): "cim.1.shared.StandardName.standards",
    (data.DataDistribution, 'responsible_party'): "cim.1.data.DataDistribution.responsible_party",
    (data.DataDistribution, 'format'): "cim.1.data.DataDistribution.format",
    (data.DataDistribution, 'access'): "cim.1.data.DataDistribution.access",
    (data.DataDistribution, 'fee'): "cim.1.data.DataDistribution.fee",
    (data.DataProperty, 'description'): "cim.1.data.DataProperty.description",
    (data.DataStorageFile, 'file_name'): "cim.1.data.DataStorageFile.file_name",
    (data.DataStorageFile, 'path'): "cim.1.data.DataStorageFile.path",
    (data.DataStorageFile, 'file_system'): "cim.1.data.DataStorageFile.file_system",
    (data.DataExtentTemporal, 'time_interval'): "cim.1.data.DataExtentTemporal.time_interval",
    (data.DataExtentTemporal, 'begin'): "cim.1.data.DataExtentTemporal.begin",
    (data.DataExtentTemporal, 'end'): "cim.1.data.DataExtentTemporal.end",
    (data.DataExtentTimeInterval, 'unit'): "cim.1.data.DataExtentTimeInterval.unit",
    (data.DataExtentTimeInterval, 'factor'): "cim.1.data.DataExtentTimeInterval.factor",
    (data.DataExtentTimeInterval, 'radix'): "cim.1.data.DataExtentTimeInterval.radix",
    (data.DataRestriction, 'license'): "cim.1.data.DataRestriction.license",
    (data.DataRestriction, 'scope'): "cim.1.data.DataRestriction.scope",
    (data.DataRestriction, 'restriction'): "cim.1.data.DataRestriction.restriction",
    (data.DataStorage, 'format'): "cim.1.data.DataStorage.format",
    (data.DataStorage, 'size'): "cim.1.data.DataStorage.size",
    (data.DataStorage, 'modification_date'): "cim.1.data.DataStorage.modification_date",
    (data.DataStorage, 'location'): "cim.1.data.DataStorage.location",
    (data.DataExtentGeographical, 'west'): "cim.1.data.DataExtentGeographical.west",
    (data.DataExtentGeographical, 'south'): "cim.1.data.DataExtentGeographical.south",
    (data.DataExtentGeographical, 'east'): "cim.1.data.DataExtentGeographical.east",
    (data.DataExtentGeographical, 'north'): "cim.1.data.DataExtentGeographical.north",
    (data.DataObject, 'distribution'): "cim.1.data.DataObject.distribution",
    (data.DataObject, 'geometry_model'): "cim.1.data.DataObject.geometry_model",
    (data.DataObject, 'purpose'): "cim.1.data.DataObject.purpose",
    (data.DataObject, 'content'): "cim.1.data.DataObject.content",
    (data.DataObject, 'source_simulation'): "cim.1.data.DataObject.source_simulation",
    (data.DataObject, 'keyword'): "cim.1.data.DataObject.keyword",
    (data.DataObject, 'data_status'): "cim.1.data.DataObject.data_status",
    (data.DataObject, 'acronym'): "cim.1.data.DataObject.acronym",
    (data.DataObject, 'meta'): "cim.1.data.DataObject.meta",
    (data.DataObject, 'extent'): "cim.1.data.DataObject.extent",
    (data.DataObject, 'properties'): "cim.1.data.DataObject.properties",
    (data.DataObject, 'description'): "cim.1.data.DataObject.description",
    (data.DataObject, 'hierarchy_level'): "cim.1.data.DataObject.hierarchy_level",
    (data.DataObject, 'storage'): "cim.1.data.DataObject.storage",
    (data.DataObject, 'restriction'): "cim.1.data.DataObject.restriction",
    (data.DataObject, 'parent_object'): "cim.1.data.DataObject.parent_object",
    (data.DataObject, 'citations'): "cim.1.data.DataObject.citations",
    (data.DataObject, 'child_object'): "cim.1.data.DataObject.child_object",
    (data.DataHierarchyLevel, 'is_open'): "cim.1.data.DataHierarchyLevel.is_open",
    (data.DataHierarchyLevel, 'value'): "cim.1.data.DataHierarchyLevel.value",
    (data.DataHierarchyLevel, 'name'): "cim.1.data.DataHierarchyLevel.name",
    (data.DataExtent, 'geographical'): "cim.1.data.DataExtent.geographical",
    (data.DataExtent, 'temporal'): "cim.1.data.DataExtent.temporal",
    (data.DataContent, 'topic'): "cim.1.data.DataContent.topic",
    (data.DataContent, 'aggregation'): "cim.1.data.DataContent.aggregation",
    (data.DataContent, 'frequency'): "cim.1.data.DataContent.frequency",
    (data.DataTopic, 'unit'): "cim.1.data.DataTopic.unit",
    (data.DataTopic, 'description'): "cim.1.data.DataTopic.description",
    (data.DataTopic, 'name'): "cim.1.data.DataTopic.name",
    (data.DataStorageDb, 'owner'): "cim.1.data.DataStorageDb.owner",
    (data.DataStorageDb, 'access_string'): "cim.1.data.DataStorageDb.access_string",
    (data.DataStorageDb, 'table'): "cim.1.data.DataStorageDb.table",
    (data.DataStorageDb, 'name'): "cim.1.data.DataStorageDb.name",
    (data.DataStorageIp, 'protocol'): "cim.1.data.DataStorageIp.protocol",
    (data.DataStorageIp, 'file_name'): "cim.1.data.DataStorageIp.file_name",
    (data.DataStorageIp, 'path'): "cim.1.data.DataStorageIp.path",
    (data.DataStorageIp, 'host'): "cim.1.data.DataStorageIp.host",
    (grids.GridExtent, 'units'): "cim.1.grids.GridExtent.units",
    (grids.GridExtent, 'minimum_longitude'): "cim.1.grids.GridExtent.minimum_longitude",
    (grids.GridExtent, 'minimum_latitude'): "cim.1.grids.GridExtent.minimum_latitude",
    (grids.GridExtent, 'maximum_latitude'): "cim.1.grids.GridExtent.maximum_latitude",
    (grids.GridExtent, 'maximum_longitude'): "cim.1.grids.GridExtent.maximum_longitude",
    (grids.GridTileResolutionType, 'description'): "cim.1.grids.GridTileResolutionType.description",
    (grids.GridTileResolutionType, 'properties'): "cim.1.grids.GridTileResolutionType.properties",
    (grids.SimpleGridGeometry, 'xcoords'): "cim.1.grids.SimpleGridGeometry.xcoords",
    (grids.SimpleGridGeometry, 'dim_order'): "cim.1.grids.SimpleGridGeometry.dim_order",
    (grids.SimpleGridGeometry, 'ycoords'): "cim.1.grids.SimpleGridGeometry.ycoords",
    (grids.SimpleGridGeometry, 'is_mesh'): "cim.1.grids.SimpleGridGeometry.is_mesh",
    (grids.SimpleGridGeometry, 'zcoords'): "cim.1.grids.SimpleGridGeometry.zcoords",
    (grids.SimpleGridGeometry, 'num_dims'): "cim.1.grids.SimpleGridGeometry.num_dims",
    (grids.GridSpec, 'esm_exchange_grids'): "cim.1.grids.GridSpec.esm_exchange_grids",
    (grids.GridSpec, 'meta'): "cim.1.grids.GridSpec.meta",
    (grids.GridSpec, 'esm_model_grids'): "cim.1.grids.GridSpec.esm_model_grids",
    (grids.CoordinateList, 'uom'): "cim.1.grids.CoordinateList.uom",
    (grids.CoordinateList, 'has_constant_offset'): "cim.1.grids.CoordinateList.has_constant_offset",
    (grids.CoordinateList, 'length'): "cim.1.grids.CoordinateList.length",
    (grids.GridTile, 'geometry_type'): "cim.1.grids.GridTile.geometry_type",
    (grids.GridTile, 'zcoords'): "cim.1.grids.GridTile.zcoords",
    (grids.GridTile, 'horizontal_resolution'): "cim.1.grids.GridTile.horizontal_resolution",
    (grids.GridTile, 'id'): "cim.1.grids.GridTile.id",
    (grids.GridTile, 'area'): "cim.1.grids.GridTile.area",
    (grids.GridTile, 'is_conformal'): "cim.1.grids.GridTile.is_conformal",
    (grids.GridTile, 'cell_array'): "cim.1.grids.GridTile.cell_array",
    (grids.GridTile, 'is_regular'): "cim.1.grids.GridTile.is_regular",
    (grids.GridTile, 'cell_ref_array'): "cim.1.grids.GridTile.cell_ref_array",
    (grids.GridTile, 'is_terrain_following'): "cim.1.grids.GridTile.is_terrain_following",
    (grids.GridTile, 'coord_file'): "cim.1.grids.GridTile.coord_file",
    (grids.GridTile, 'is_uniform'): "cim.1.grids.GridTile.is_uniform",
    (grids.GridTile, 'coordinate_pole'): "cim.1.grids.GridTile.coordinate_pole",
    (grids.GridTile, 'long_name'): "cim.1.grids.GridTile.long_name",
    (grids.GridTile, 'horizontal_crs'): "cim.1.grids.GridTile.horizontal_crs",
    (grids.GridTile, 'vertical_crs'): "cim.1.grids.GridTile.vertical_crs",
    (grids.GridTile, 'mnemonic'): "cim.1.grids.GridTile.mnemonic",
    (grids.GridTile, 'grid_north_pole'): "cim.1.grids.GridTile.grid_north_pole",
    (grids.GridTile, 'nx'): "cim.1.grids.GridTile.nx",
    (grids.GridTile, 'simple_grid_geom'): "cim.1.grids.GridTile.simple_grid_geom",
    (grids.GridTile, 'ny'): "cim.1.grids.GridTile.ny",
    (grids.GridTile, 'nz'): "cim.1.grids.GridTile.nz",
    (grids.GridTile, 'description'): "cim.1.grids.GridTile.description",
    (grids.GridTile, 'discretization_type'): "cim.1.grids.GridTile.discretization_type",
    (grids.GridTile, 'short_name'): "cim.1.grids.GridTile.short_name",
    (grids.GridTile, 'refinement_scheme'): "cim.1.grids.GridTile.refinement_scheme",
    (grids.GridTile, 'extent'): "cim.1.grids.GridTile.extent",
    (grids.GridTile, 'vertical_resolution'): "cim.1.grids.GridTile.vertical_resolution",
    (grids.GridMosaic, 'short_name'): "cim.1.grids.GridMosaic.short_name",
    (grids.GridMosaic, 'id'): "cim.1.grids.GridMosaic.id",
    (grids.GridMosaic, 'mnemonic'): "cim.1.grids.GridMosaic.mnemonic",
    (grids.GridMosaic, 'mosaics'): "cim.1.grids.GridMosaic.mosaics",
    (grids.GridMosaic, 'type'): "cim.1.grids.GridMosaic.type",
    (grids.GridMosaic, 'is_leaf'): "cim.1.grids.GridMosaic.is_leaf",
    (grids.GridMosaic, 'description'): "cim.1.grids.GridMosaic.description",
    (grids.GridMosaic, 'tile_count'): "cim.1.grids.GridMosaic.tile_count",
    (grids.GridMosaic, 'extent'): "cim.1.grids.GridMosaic.extent",
    (grids.GridMosaic, 'long_name'): "cim.1.grids.GridMosaic.long_name",
    (grids.GridMosaic, 'mosaic_count'): "cim.1.grids.GridMosaic.mosaic_count",
    (grids.GridMosaic, 'tiles'): "cim.1.grids.GridMosaic.tiles",
    (grids.GridMosaic, 'has_congruent_tiles'): "cim.1.grids.GridMosaic.has_congruent_tiles",
    (grids.GridMosaic, 'citations'): "cim.1.grids.GridMosaic.citations",
    (grids.VerticalCoordinateList, 'form'): "cim.1.grids.VerticalCoordinateList.form",
    (grids.VerticalCoordinateList, 'type'): "cim.1.grids.VerticalCoordinateList.type",
    (grids.VerticalCoordinateList, 'properties'): "cim.1.grids.VerticalCoordinateList.properties",
    (quality.Measure, 'description'): "cim.1.quality.Measure.description",
    (quality.Measure, 'name'): "cim.1.quality.Measure.name",
    (quality.Measure, 'identification'): "cim.1.quality.Measure.identification",
    (quality.Report, 'evaluator'): "cim.1.quality.Report.evaluator",
    (quality.Report, 'date'): "cim.1.quality.Report.date",
    (quality.Report, 'measure'): "cim.1.quality.Report.measure",
    (quality.Report, 'evaluation'): "cim.1.quality.Report.evaluation",
    (quality.CimQuality, 'meta'): "cim.1.quality.CimQuality.meta",
    (quality.CimQuality, 'reports'): "cim.1.quality.CimQuality.reports",
    (quality.Evaluation, 'date'): "cim.1.quality.Evaluation.date",
    (quality.Evaluation, 'type'): "cim.1.quality.Evaluation.type",
    (quality.Evaluation, 'specification'): "cim.1.quality.Evaluation.specification",
    (quality.Evaluation, 'specification_hyperlink'): "cim.1.quality.Evaluation.specification_hyperlink",
    (quality.Evaluation, 'title'): "cim.1.quality.Evaluation.title",
    (quality.Evaluation, 'did_pass'): "cim.1.quality.Evaluation.did_pass",
    (quality.Evaluation, 'type_hyperlink'): "cim.1.quality.Evaluation.type_hyperlink",
    (quality.Evaluation, 'description'): "cim.1.quality.Evaluation.description",
    (quality.Evaluation, 'explanation'): "cim.1.quality.Evaluation.explanation",
    (misc.DocumentSet, 'data'): "cim.1.misc.DocumentSet.data",
    (misc.DocumentSet, 'grids'): "cim.1.misc.DocumentSet.grids",
    (misc.DocumentSet, 'model'): "cim.1.misc.DocumentSet.model",
    (misc.DocumentSet, 'meta'): "cim.1.misc.DocumentSet.meta",
    (misc.DocumentSet, 'platform'): "cim.1.misc.DocumentSet.platform",
    (misc.DocumentSet, 'ensembles'): "cim.1.misc.DocumentSet.ensembles",
    (misc.DocumentSet, 'simulation'): "cim.1.misc.DocumentSet.simulation",
    (misc.DocumentSet, 'experiment'): "cim.1.misc.DocumentSet.experiment",
    (activity.Experiment, 'measurement_campaigns'): "cim.1.activity.Experiment.measurement_campaigns",
    (activity.Experiment, 'supports'): "cim.1.activity.Experiment.supports",
    (activity.Experiment, 'generates'): "cim.1.activity.Experiment.generates",
    (activity.Experiment, 'requires'): "cim.1.activity.Experiment.requires",
    (activity.SimulationRelationship, 'target'): "cim.1.activity.SimulationRelationship.target",
    (activity.SimulationRelationship, 'type'): "cim.1.activity.SimulationRelationship.type",
    (activity.DownscalingSimulation, 'downscaling_type'): "cim.1.activity.DownscalingSimulation.downscaling_type",
    (activity.DownscalingSimulation, 'meta'): "cim.1.activity.DownscalingSimulation.meta",
    (activity.DownscalingSimulation, 'outputs'): "cim.1.activity.DownscalingSimulation.outputs",
    (activity.DownscalingSimulation, 'downscaling_id'): "cim.1.activity.DownscalingSimulation.downscaling_id",
    (activity.DownscalingSimulation, 'downscaled_from'): "cim.1.activity.DownscalingSimulation.downscaled_from",
    (activity.DownscalingSimulation, 'calendar'): "cim.1.activity.DownscalingSimulation.calendar",
    (activity.DownscalingSimulation, 'inputs'): "cim.1.activity.DownscalingSimulation.inputs",
    (activity.NumericalRequirement, 'options'): "cim.1.activity.NumericalRequirement.options",
    (activity.NumericalRequirement, 'id'): "cim.1.activity.NumericalRequirement.id",
    (activity.NumericalRequirement, 'description'): "cim.1.activity.NumericalRequirement.description",
    (activity.NumericalRequirement, 'source'): "cim.1.activity.NumericalRequirement.source",
    (activity.NumericalRequirement, 'requirement_type'): "cim.1.activity.NumericalRequirement.requirement_type",
    (activity.NumericalRequirement, 'name'): "cim.1.activity.NumericalRequirement.name",
    (activity.EnsembleMember, 'simulation'): "cim.1.activity.EnsembleMember.simulation",
    (activity.EnsembleMember, 'ensemble'): "cim.1.activity.EnsembleMember.ensemble",
    (activity.EnsembleMember, 'ensemble_ids'): "cim.1.activity.EnsembleMember.ensemble_ids",
    (activity.NumericalActivity, 'supports'): "cim.1.activity.NumericalActivity.supports",
    (activity.NumericalActivity, 'description'): "cim.1.activity.NumericalActivity.description",
    (activity.NumericalActivity, 'short_name'): "cim.1.activity.NumericalActivity.short_name",
    (activity.NumericalActivity, 'long_name'): "cim.1.activity.NumericalActivity.long_name",
    (activity.Simulation, 'restarts'): "cim.1.activity.Simulation.restarts",
    (activity.Simulation, 'inputs'): "cim.1.activity.Simulation.inputs",
    (activity.Simulation, 'spinup_date_range'): "cim.1.activity.Simulation.spinup_date_range",
    (activity.Simulation, 'control_simulation'): "cim.1.activity.Simulation.control_simulation",
    (activity.Simulation, 'authors'): "cim.1.activity.Simulation.authors",
    (activity.Simulation, 'spinup_simulation'): "cim.1.activity.Simulation.spinup_simulation",
    (activity.Simulation, 'simulation_id'): "cim.1.activity.Simulation.simulation_id",
    (activity.Simulation, 'outputs'): "cim.1.activity.Simulation.outputs",
    (activity.Simulation, 'conformances'): "cim.1.activity.Simulation.conformances",
    (activity.Simulation, 'deployments'): "cim.1.activity.Simulation.deployments",
    (activity.Simulation, 'calendar'): "cim.1.activity.Simulation.calendar",
    (activity.ExperimentRelationship, 'target'): "cim.1.activity.ExperimentRelationship.target",
    (activity.ExperimentRelationship, 'type'): "cim.1.activity.ExperimentRelationship.type",
    (activity.ExperimentRelationshipTarget, 'numerical_experiment'): "cim.1.activity.ExperimentRelationshipTarget.numerical_experiment",
    (activity.NumericalRequirementOption, 'sub_options'): "cim.1.activity.NumericalRequirementOption.sub_options",
    (activity.NumericalRequirementOption, 'name'): "cim.1.activity.NumericalRequirementOption.name",
    (activity.NumericalRequirementOption, 'relationship'): "cim.1.activity.NumericalRequirementOption.relationship",
    (activity.NumericalRequirementOption, 'description'): "cim.1.activity.NumericalRequirementOption.description",
    (activity.NumericalRequirementOption, 'id'): "cim.1.activity.NumericalRequirementOption.id",
    (activity.Activity, 'responsible_parties'): "cim.1.activity.Activity.responsible_parties",
    (activity.Activity, 'funding_sources'): "cim.1.activity.Activity.funding_sources",
    (activity.Activity, 'rationales'): "cim.1.activity.Activity.rationales",
    (activity.Activity, 'projects'): "cim.1.activity.Activity.projects",
    (activity.SimulationRelationshipTarget, 'simulation'): "cim.1.activity.SimulationRelationshipTarget.simulation",
    (activity.SimulationRelationshipTarget, 'target'): "cim.1.activity.SimulationRelationshipTarget.target",
    (activity.SpatioTemporalConstraint, 'date_range'): "cim.1.activity.SpatioTemporalConstraint.date_range",
    (activity.SpatioTemporalConstraint, 'spatial_resolution'): "cim.1.activity.SpatioTemporalConstraint.spatial_resolution",
    (activity.MeasurementCampaign, 'duration'): "cim.1.activity.MeasurementCampaign.duration",
    (activity.Conformance, 'description'): "cim.1.activity.Conformance.description",
    (activity.Conformance, 'sources'): "cim.1.activity.Conformance.sources",
    (activity.Conformance, 'frequency'): "cim.1.activity.Conformance.frequency",
    (activity.Conformance, 'type'): "cim.1.activity.Conformance.type",
    (activity.Conformance, 'is_conformant'): "cim.1.activity.Conformance.is_conformant",
    (activity.Conformance, 'requirements'): "cim.1.activity.Conformance.requirements",
    (activity.Ensemble, 'outputs'): "cim.1.activity.Ensemble.outputs",
    (activity.Ensemble, 'members'): "cim.1.activity.Ensemble.members",
    (activity.Ensemble, 'types'): "cim.1.activity.Ensemble.types",
    (activity.Ensemble, 'meta'): "cim.1.activity.Ensemble.meta",
    (activity.SimulationRun, 'model'): "cim.1.activity.SimulationRun.model",
    (activity.SimulationRun, 'date_range'): "cim.1.activity.SimulationRun.date_range",
    (activity.SimulationRun, 'meta'): "cim.1.activity.SimulationRun.meta",
    (activity.SimulationComposite, 'meta'): "cim.1.activity.SimulationComposite.meta",
    (activity.SimulationComposite, 'rank'): "cim.1.activity.SimulationComposite.rank",
    (activity.SimulationComposite, 'child'): "cim.1.activity.SimulationComposite.child",
    (activity.SimulationComposite, 'date_range'): "cim.1.activity.SimulationComposite.date_range",
    (activity.NumericalExperiment, 'requirements'): "cim.1.activity.NumericalExperiment.requirements",
    (activity.NumericalExperiment, 'meta'): "cim.1.activity.NumericalExperiment.meta",
    (activity.NumericalExperiment, 'description'): "cim.1.activity.NumericalExperiment.description",
    (activity.NumericalExperiment, 'short_name'): "cim.1.activity.NumericalExperiment.short_name",
    (activity.NumericalExperiment, 'experiment_id'): "cim.1.activity.NumericalExperiment.experiment_id",
    (activity.NumericalExperiment, 'long_name'): "cim.1.activity.NumericalExperiment.long_name",
    (software.Coupling, 'target'): "cim.1.software.Coupling.target",
    (software.Coupling, 'priming'): "cim.1.software.Coupling.priming",
    (software.Coupling, 'time_lag'): "cim.1.software.Coupling.time_lag",
    (software.Coupling, 'type'): "cim.1.software.Coupling.type",
    (software.Coupling, 'sources'): "cim.1.software.Coupling.sources",
    (software.Coupling, 'connections'): "cim.1.software.Coupling.connections",
    (software.Coupling, 'spatial_regriddings'): "cim.1.software.Coupling.spatial_regriddings",
    (software.Coupling, 'description'): "cim.1.software.Coupling.description",
    (software.Coupling, 'properties'): "cim.1.software.Coupling.properties",
    (software.Coupling, 'time_transformation'): "cim.1.software.Coupling.time_transformation",
    (software.Coupling, 'transformers'): "cim.1.software.Coupling.transformers",
    (software.Coupling, 'purpose'): "cim.1.software.Coupling.purpose",
    (software.Coupling, 'time_profile'): "cim.1.software.Coupling.time_profile",
    (software.Coupling, 'is_fully_specified'): "cim.1.software.Coupling.is_fully_specified",
    (software.Parallelisation, 'processes'): "cim.1.software.Parallelisation.processes",
    (software.Parallelisation, 'ranks'): "cim.1.software.Parallelisation.ranks",
    (software.SpatialRegridding, 'user_method'): "cim.1.software.SpatialRegridding.user_method",
    (software.SpatialRegridding, 'standard_method'): "cim.1.software.SpatialRegridding.standard_method",
    (software.SpatialRegridding, 'dimension'): "cim.1.software.SpatialRegridding.dimension",
    (software.SpatialRegridding, 'properties'): "cim.1.software.SpatialRegridding.properties",
    (software.EntryPoint, 'name'): "cim.1.software.EntryPoint.name",
    (software.ProcessorComponent, 'meta'): "cim.1.software.ProcessorComponent.meta",
    (software.StatisticalModelComponent, 'meta'): "cim.1.software.StatisticalModelComponent.meta",
    (software.StatisticalModelComponent, 'types'): "cim.1.software.StatisticalModelComponent.types",
    (software.StatisticalModelComponent, 'type'): "cim.1.software.StatisticalModelComponent.type",
    (software.StatisticalModelComponent, 'timing'): "cim.1.software.StatisticalModelComponent.timing",
    (software.Composition, 'couplings'): "cim.1.software.Composition.couplings",
    (software.Composition, 'description'): "cim.1.software.Composition.description",
    (software.Timing, 'start'): "cim.1.software.Timing.start",
    (software.Timing, 'units'): "cim.1.software.Timing.units",
    (software.Timing, 'end'): "cim.1.software.Timing.end",
    (software.Timing, 'rate'): "cim.1.software.Timing.rate",
    (software.Timing, 'is_variable_rate'): "cim.1.software.Timing.is_variable_rate",
    (software.ComponentLanguage, 'name'): "cim.1.software.ComponentLanguage.name",
    (software.ComponentLanguage, 'properties'): "cim.1.software.ComponentLanguage.properties",
    (software.SpatialRegriddingUserMethod, 'file'): "cim.1.software.SpatialRegriddingUserMethod.file",
    (software.SpatialRegriddingUserMethod, 'name'): "cim.1.software.SpatialRegriddingUserMethod.name",
    (software.ComponentProperty, 'values'): "cim.1.software.ComponentProperty.values",
    (software.ComponentProperty, 'grid'): "cim.1.software.ComponentProperty.grid",
    (software.ComponentProperty, 'sub_properties'): "cim.1.software.ComponentProperty.sub_properties",
    (software.ComponentProperty, 'standard_names'): "cim.1.software.ComponentProperty.standard_names",
    (software.ComponentProperty, 'intent'): "cim.1.software.ComponentProperty.intent",
    (software.ComponentProperty, 'description'): "cim.1.software.ComponentProperty.description",
    (software.ComponentProperty, 'units'): "cim.1.software.ComponentProperty.units",
    (software.ComponentProperty, 'citations'): "cim.1.software.ComponentProperty.citations",
    (software.ComponentProperty, 'short_name'): "cim.1.software.ComponentProperty.short_name",
    (software.ComponentProperty, 'long_name'): "cim.1.software.ComponentProperty.long_name",
    (software.ComponentProperty, 'is_represented'): "cim.1.software.ComponentProperty.is_represented",
    (software.TimeTransformation, 'description'): "cim.1.software.TimeTransformation.description",
    (software.TimeTransformation, 'mapping_type'): "cim.1.software.TimeTransformation.mapping_type",
    (software.Deployment, 'parallelisation'): "cim.1.software.Deployment.parallelisation",
    (software.Deployment, 'platform'): "cim.1.software.Deployment.platform",
    (software.Deployment, 'description'): "cim.1.software.Deployment.description",
    (software.Deployment, 'executable_name'): "cim.1.software.Deployment.executable_name",
    (software.Deployment, 'executable_arguments'): "cim.1.software.Deployment.executable_arguments",
    (software.Deployment, 'deployment_date'): "cim.1.software.Deployment.deployment_date",
    (software.Component, 'dependencies'): "cim.1.software.Component.dependencies",
    (software.Component, 'version'): "cim.1.software.Component.version",
    (software.Component, 'deployments'): "cim.1.software.Component.deployments",
    (software.Component, 'description'): "cim.1.software.Component.description",
    (software.Component, 'funding_sources'): "cim.1.software.Component.funding_sources",
    (software.Component, 'grid'): "cim.1.software.Component.grid",
    (software.Component, 'is_embedded'): "cim.1.software.Component.is_embedded",
    (software.Component, 'language'): "cim.1.software.Component.language",
    (software.Component, 'license'): "cim.1.software.Component.license",
    (software.Component, 'long_name'): "cim.1.software.Component.long_name",
    (software.Component, 'online_resource'): "cim.1.software.Component.online_resource",
    (software.Component, 'parent'): "cim.1.software.Component.parent",
    (software.Component, 'sub_components'): "cim.1.software.Component.sub_components",
    (software.Component, 'previous_version'): "cim.1.software.Component.previous_version",
    (software.Component, 'citations'): "cim.1.software.Component.citations",
    (software.Component, 'properties'): "cim.1.software.Component.properties",
    (software.Component, 'code_access'): "cim.1.software.Component.code_access",
    (software.Component, 'release_date'): "cim.1.software.Component.release_date",
    (software.Component, 'composition'): "cim.1.software.Component.composition",
    (software.Component, 'responsible_parties'): "cim.1.software.Component.responsible_parties",
    (software.Component, 'coupling_framework'): "cim.1.software.Component.coupling_framework",
    (software.Component, 'short_name'): "cim.1.software.Component.short_name",
    (software.ModelComponent, 'activity'): "cim.1.software.ModelComponent.activity",
    (software.ModelComponent, 'type'): "cim.1.software.ModelComponent.type",
    (software.ModelComponent, 'meta'): "cim.1.software.ModelComponent.meta",
    (software.ModelComponent, 'types'): "cim.1.software.ModelComponent.types",
    (software.ModelComponent, 'timing'): "cim.1.software.ModelComponent.timing",
    (software.Rank, 'increment'): "cim.1.software.Rank.increment",
    (software.Rank, 'min'): "cim.1.software.Rank.min",
    (software.Rank, 'value'): "cim.1.software.Rank.value",
    (software.Rank, 'max'): "cim.1.software.Rank.max",
    (software.CouplingEndpoint, 'properties'): "cim.1.software.CouplingEndpoint.properties",
    (software.CouplingEndpoint, 'data_source'): "cim.1.software.CouplingEndpoint.data_source",
    (software.CouplingEndpoint, 'instance_id'): "cim.1.software.CouplingEndpoint.instance_id",
    (software.TimeLag, 'units'): "cim.1.software.TimeLag.units",
    (software.TimeLag, 'value'): "cim.1.software.TimeLag.value",
    (software.Connection, 'target'): "cim.1.software.Connection.target",
    (software.Connection, 'transformers'): "cim.1.software.Connection.transformers",
    (software.Connection, 'priming'): "cim.1.software.Connection.priming",
    (software.Connection, 'description'): "cim.1.software.Connection.description",
    (software.Connection, 'time_profile'): "cim.1.software.Connection.time_profile",
    (software.Connection, 'properties'): "cim.1.software.Connection.properties",
    (software.Connection, 'time_transformation'): "cim.1.software.Connection.time_transformation",
    (software.Connection, 'sources'): "cim.1.software.Connection.sources",
    (software.Connection, 'spatial_regridding'): "cim.1.software.Connection.spatial_regridding",
    (software.Connection, 'type'): "cim.1.software.Connection.type",
    (software.Connection, 'time_lag'): "cim.1.software.Connection.time_lag",
    (software.ConnectionEndpoint, 'properties'): "cim.1.software.ConnectionEndpoint.properties",
    (software.ConnectionEndpoint, 'data_source'): "cim.1.software.ConnectionEndpoint.data_source",
    (software.ConnectionEndpoint, 'instance_id'): "cim.1.software.ConnectionEndpoint.instance_id",

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    shared.InterconnectType: "cim.1.shared.InterconnectType",
    shared.OperatingSystemType: "cim.1.shared.OperatingSystemType",
    shared.DocRelationshipDirectionType: "cim.1.shared.DocRelationshipDirectionType",
    shared.DataPurpose: "cim.1.shared.DataPurpose",
    shared.DocStatusType: "cim.1.shared.DocStatusType",
    shared.UnitType: "cim.1.shared.UnitType",
    shared.CompilerType: "cim.1.shared.CompilerType",
    shared.DocRelationshipType: "cim.1.shared.DocRelationshipType",
    shared.MachineVendorType: "cim.1.shared.MachineVendorType",
    shared.DocType: "cim.1.shared.DocType",
    shared.ChangePropertyType: "cim.1.shared.ChangePropertyType",
    shared.ProcessorType: "cim.1.shared.ProcessorType",
    shared.MachineType: "cim.1.shared.MachineType",
    data.DataHierarchyType: "cim.1.data.DataHierarchyType",
    data.DataStatusType: "cim.1.data.DataStatusType",
    grids.DiscretizationEnum: "cim.1.grids.DiscretizationEnum",
    grids.HorizontalCsEnum: "cim.1.grids.HorizontalCsEnum",
    grids.ArcTypeEnum: "cim.1.grids.ArcTypeEnum",
    grids.VerticalCsEnum: "cim.1.grids.VerticalCsEnum",
    grids.RefinementTypeEnum: "cim.1.grids.RefinementTypeEnum",
    grids.GridNodePositionEnum: "cim.1.grids.GridNodePositionEnum",
    grids.GridTypeEnum: "cim.1.grids.GridTypeEnum",
    grids.FeatureTypeEnum: "cim.1.grids.FeatureTypeEnum",
    grids.GeometryTypeEnum: "cim.1.grids.GeometryTypeEnum",
    quality.CimFeatureType: "cim.1.quality.CimFeatureType",
    quality.CimScopeCodeType: "cim.1.quality.CimScopeCodeType",
    quality.QualityStatusType: "cim.1.quality.QualityStatusType",
    quality.CimResultType: "cim.1.quality.CimResultType",
    quality.QualitySeverityType: "cim.1.quality.QualitySeverityType",
    quality.QualityIssueType: "cim.1.quality.QualityIssueType",
    activity.EnsembleType: "cim.1.activity.EnsembleType",
    activity.ExperimentRelationshipType: "cim.1.activity.ExperimentRelationshipType",
    activity.DownscalingType: "cim.1.activity.DownscalingType",
    activity.FrequencyType: "cim.1.activity.FrequencyType",
    activity.ProjectType: "cim.1.activity.ProjectType",
    activity.ResolutionType: "cim.1.activity.ResolutionType",
    activity.SimulationType: "cim.1.activity.SimulationType",
    activity.ConformanceType: "cim.1.activity.ConformanceType",
    activity.SimulationRelationshipType: "cim.1.activity.SimulationRelationshipType",
    software.ModelComponentType: "cim.1.software.ModelComponentType",
    software.StatisticalModelComponentType: "cim.1.software.StatisticalModelComponentType",
    software.SpatialRegriddingDimensionType: "cim.1.software.SpatialRegriddingDimensionType",
    software.CouplingFrameworkType: "cim.1.software.CouplingFrameworkType",
    software.SpatialRegriddingStandardMethodType: "cim.1.software.SpatialRegriddingStandardMethodType",
    software.TimeMappingType: "cim.1.software.TimeMappingType",
    software.ConnectionType: "cim.1.software.ConnectionType",
    software.TimingUnits: "cim.1.software.TimingUnits",
    software.ComponentPropertyIntentType: "cim.1.software.ComponentPropertyIntentType",

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (shared.DocRelationshipDirectionType, 'toTarget'): "cim.1.shared.DocRelationshipDirectionType.toTarget",
    (shared.DocRelationshipDirectionType, 'fromTarget'): "cim.1.shared.DocRelationshipDirectionType.fromTarget",
    (shared.DataPurpose, 'boundaryCondition'): "cim.1.shared.DataPurpose.boundaryCondition",
    (shared.DataPurpose, 'ancillaryFile'): "cim.1.shared.DataPurpose.ancillaryFile",
    (shared.DataPurpose, 'initialCondition'): "cim.1.shared.DataPurpose.initialCondition",
    (shared.DocStatusType, 'incomplete'): "cim.1.shared.DocStatusType.incomplete",
    (shared.DocStatusType, 'complete'): "cim.1.shared.DocStatusType.complete",
    (shared.DocStatusType, 'in-progress'): "cim.1.shared.DocStatusType.in-progress",
    (shared.DocRelationshipType, 'other'): "cim.1.shared.DocRelationshipType.other",
    (shared.DocRelationshipType, 'similarTo'): "cim.1.shared.DocRelationshipType.similarTo",
    (shared.DocRelationshipType, 'previousVersionOf'): "cim.1.shared.DocRelationshipType.previousVersionOf",
    (shared.DocRelationshipType, 'fixedVersionOf'): "cim.1.shared.DocRelationshipType.fixedVersionOf",
    (shared.DocRelationshipType, 'laterVersionOf'): "cim.1.shared.DocRelationshipType.laterVersionOf",
    (shared.DocType, 'dataObject'): "cim.1.shared.DocType.dataObject",
    (shared.DocType, 'simulationComposite'): "cim.1.shared.DocType.simulationComposite",
    (shared.DocType, 'gridSpec'): "cim.1.shared.DocType.gridSpec",
    (shared.DocType, 'processorComponent'): "cim.1.shared.DocType.processorComponent",
    (shared.DocType, 'cimQuality'): "cim.1.shared.DocType.cimQuality",
    (shared.DocType, 'assimilation'): "cim.1.shared.DocType.assimilation",
    (shared.DocType, 'downscalingSimulation'): "cim.1.shared.DocType.downscalingSimulation",
    (shared.DocType, 'platform'): "cim.1.shared.DocType.platform",
    (shared.DocType, 'modelComponent'): "cim.1.shared.DocType.modelComponent",
    (shared.DocType, 'simulationRun'): "cim.1.shared.DocType.simulationRun",
    (shared.DocType, 'dataProcessing'): "cim.1.shared.DocType.dataProcessing",
    (shared.DocType, 'statisticalModelComponent'): "cim.1.shared.DocType.statisticalModelComponent",
    (shared.DocType, 'ensemble'): "cim.1.shared.DocType.ensemble",
    (shared.DocType, 'numericalExperiment'): "cim.1.shared.DocType.numericalExperiment",
    (shared.ChangePropertyType, 'BoundaryCondition'): "cim.1.shared.ChangePropertyType.BoundaryCondition",
    (shared.ChangePropertyType, 'InitialCondition'): "cim.1.shared.ChangePropertyType.InitialCondition",
    (shared.ChangePropertyType, 'ModelMod'): "cim.1.shared.ChangePropertyType.ModelMod",
    (shared.ChangePropertyType, 'Increment'): "cim.1.shared.ChangePropertyType.Increment",
    (shared.ChangePropertyType, 'Redistribution'): "cim.1.shared.ChangePropertyType.Redistribution",
    (shared.ChangePropertyType, 'InputMod'): "cim.1.shared.ChangePropertyType.InputMod",
    (shared.ChangePropertyType, 'Replacement'): "cim.1.shared.ChangePropertyType.Replacement",
    (shared.ChangePropertyType, 'ParameterChange'): "cim.1.shared.ChangePropertyType.ParameterChange",
    (shared.ChangePropertyType, 'Unused'): "cim.1.shared.ChangePropertyType.Unused",
    (shared.ChangePropertyType, 'CodeChange'): "cim.1.shared.ChangePropertyType.CodeChange",
    (shared.ChangePropertyType, 'AncillaryFile'): "cim.1.shared.ChangePropertyType.AncillaryFile",
    (shared.ChangePropertyType, 'Decrement'): "cim.1.shared.ChangePropertyType.Decrement",
    (shared.MachineType, 'Beowulf'): "cim.1.shared.MachineType.Beowulf",
    (shared.MachineType, 'Vector'): "cim.1.shared.MachineType.Vector",
    (shared.MachineType, 'Parallel'): "cim.1.shared.MachineType.Parallel",
    (data.DataStatusType, 'complete'): "cim.1.data.DataStatusType.complete",
    (data.DataStatusType, 'metadataOnly'): "cim.1.data.DataStatusType.metadataOnly",
    (data.DataStatusType, 'continuouslySupplemented'): "cim.1.data.DataStatusType.continuouslySupplemented",
    (grids.DiscretizationEnum, 'structured_triangular'): "cim.1.grids.DiscretizationEnum.structured_triangular",
    (grids.DiscretizationEnum, 'unstructured_triangular'): "cim.1.grids.DiscretizationEnum.unstructured_triangular",
    (grids.DiscretizationEnum, 'pixel-based_catchment'): "cim.1.grids.DiscretizationEnum.pixel-based_catchment",
    (grids.DiscretizationEnum, 'unstructured_polygonal'): "cim.1.grids.DiscretizationEnum.unstructured_polygonal",
    (grids.DiscretizationEnum, 'spherical_harmonics'): "cim.1.grids.DiscretizationEnum.spherical_harmonics",
    (grids.DiscretizationEnum, 'other'): "cim.1.grids.DiscretizationEnum.other",
    (grids.DiscretizationEnum, 'logically_rectangular'): "cim.1.grids.DiscretizationEnum.logically_rectangular",
    (grids.HorizontalCsEnum, 'spherical'): "cim.1.grids.HorizontalCsEnum.spherical",
    (grids.HorizontalCsEnum, 'cartesian'): "cim.1.grids.HorizontalCsEnum.cartesian",
    (grids.HorizontalCsEnum, 'ellipsoidal'): "cim.1.grids.HorizontalCsEnum.ellipsoidal",
    (grids.HorizontalCsEnum, 'polar'): "cim.1.grids.HorizontalCsEnum.polar",
    (grids.ArcTypeEnum, 'complex'): "cim.1.grids.ArcTypeEnum.complex",
    (grids.ArcTypeEnum, 'geodesic'): "cim.1.grids.ArcTypeEnum.geodesic",
    (grids.ArcTypeEnum, 'small_circle'): "cim.1.grids.ArcTypeEnum.small_circle",
    (grids.ArcTypeEnum, 'great_circle'): "cim.1.grids.ArcTypeEnum.great_circle",
    (grids.VerticalCsEnum, 'mass-based'): "cim.1.grids.VerticalCsEnum.mass-based",
    (grids.VerticalCsEnum, 'space-based'): "cim.1.grids.VerticalCsEnum.space-based",
    (grids.RefinementTypeEnum, 'none'): "cim.1.grids.RefinementTypeEnum.none",
    (grids.RefinementTypeEnum, 'integer'): "cim.1.grids.RefinementTypeEnum.integer",
    (grids.RefinementTypeEnum, 'rational'): "cim.1.grids.RefinementTypeEnum.rational",
    (grids.GridNodePositionEnum, 'plane'): "cim.1.grids.GridNodePositionEnum.plane",
    (grids.GridNodePositionEnum, 'centre'): "cim.1.grids.GridNodePositionEnum.centre",
    (grids.GridNodePositionEnum, 'sphere'): "cim.1.grids.GridNodePositionEnum.sphere",
    (grids.GridTypeEnum, 'displaced_pole'): "cim.1.grids.GridTypeEnum.displaced_pole",
    (grids.GridTypeEnum, 'icosahedral_geodesic'): "cim.1.grids.GridTypeEnum.icosahedral_geodesic",
    (grids.GridTypeEnum, 'reduced_gaussian'): "cim.1.grids.GridTypeEnum.reduced_gaussian",
    (grids.GridTypeEnum, 'regular_lat_lon'): "cim.1.grids.GridTypeEnum.regular_lat_lon",
    (grids.GridTypeEnum, 'cubed_sphere'): "cim.1.grids.GridTypeEnum.cubed_sphere",
    (grids.GridTypeEnum, 'spectral_gaussian'): "cim.1.grids.GridTypeEnum.spectral_gaussian",
    (grids.GridTypeEnum, 'tripolar'): "cim.1.grids.GridTypeEnum.tripolar",
    (grids.GridTypeEnum, 'yin_yang'): "cim.1.grids.GridTypeEnum.yin_yang",
    (grids.GridTypeEnum, 'composite'): "cim.1.grids.GridTypeEnum.composite",
    (grids.GridTypeEnum, 'other'): "cim.1.grids.GridTypeEnum.other",
    (grids.FeatureTypeEnum, 'edge'): "cim.1.grids.FeatureTypeEnum.edge",
    (grids.FeatureTypeEnum, 'point'): "cim.1.grids.FeatureTypeEnum.point",
    (grids.GeometryTypeEnum, 'plane'): "cim.1.grids.GeometryTypeEnum.plane",
    (grids.GeometryTypeEnum, 'ellipsoid'): "cim.1.grids.GeometryTypeEnum.ellipsoid",
    (grids.GeometryTypeEnum, 'sphere'): "cim.1.grids.GeometryTypeEnum.sphere",
    (quality.CimFeatureType, 'diagnostic'): "cim.1.quality.CimFeatureType.diagnostic",
    (quality.CimFeatureType, 'file'): "cim.1.quality.CimFeatureType.file",
    (quality.CimScopeCodeType, 'model'): "cim.1.quality.CimScopeCodeType.model",
    (quality.CimScopeCodeType, 'modelComponent'): "cim.1.quality.CimScopeCodeType.modelComponent",
    (quality.CimScopeCodeType, 'simulation'): "cim.1.quality.CimScopeCodeType.simulation",
    (quality.CimScopeCodeType, 'experiment'): "cim.1.quality.CimScopeCodeType.experiment",
    (quality.CimScopeCodeType, 'numericalRequirement'): "cim.1.quality.CimScopeCodeType.numericalRequirement",
    (quality.CimScopeCodeType, 'dataset'): "cim.1.quality.CimScopeCodeType.dataset",
    (quality.CimScopeCodeType, 'software'): "cim.1.quality.CimScopeCodeType.software",
    (quality.CimScopeCodeType, 'file'): "cim.1.quality.CimScopeCodeType.file",
    (quality.CimScopeCodeType, 'service'): "cim.1.quality.CimScopeCodeType.service",
    (quality.CimScopeCodeType, 'ensemble'): "cim.1.quality.CimScopeCodeType.ensemble",
    (quality.QualityStatusType, 'partially_resolved'): "cim.1.quality.QualityStatusType.partially_resolved",
    (quality.QualityStatusType, 'resolved'): "cim.1.quality.QualityStatusType.resolved",
    (quality.QualityStatusType, 'confirmed'): "cim.1.quality.QualityStatusType.confirmed",
    (quality.QualityStatusType, 'reported'): "cim.1.quality.QualityStatusType.reported",
    (quality.CimResultType, 'document'): "cim.1.quality.CimResultType.document",
    (quality.CimResultType, 'logfile'): "cim.1.quality.CimResultType.logfile",
    (quality.CimResultType, 'plot'): "cim.1.quality.CimResultType.plot",
    (quality.QualitySeverityType, 'minor'): "cim.1.quality.QualitySeverityType.minor",
    (quality.QualitySeverityType, 'cosmetic'): "cim.1.quality.QualitySeverityType.cosmetic",
    (quality.QualitySeverityType, 'major'): "cim.1.quality.QualitySeverityType.major",
    (quality.QualityIssueType, 'metadata'): "cim.1.quality.QualityIssueType.metadata",
    (quality.QualityIssueType, 'data_content'): "cim.1.quality.QualityIssueType.data_content",
    (quality.QualityIssueType, 'science'): "cim.1.quality.QualityIssueType.science",
    (quality.QualityIssueType, 'data_format'): "cim.1.quality.QualityIssueType.data_format",
    (quality.QualityIssueType, 'data_indexing'): "cim.1.quality.QualityIssueType.data_indexing",
    (activity.ExperimentRelationshipType, 'modifiedInputMethodOf'): "cim.1.activity.ExperimentRelationshipType.modifiedInputMethodOf",
    (activity.ExperimentRelationshipType, 'shorterVersionOf'): "cim.1.activity.ExperimentRelationshipType.shorterVersionOf",
    (activity.ExperimentRelationshipType, 'extensionOf'): "cim.1.activity.ExperimentRelationshipType.extensionOf",
    (activity.ExperimentRelationshipType, 'continuationOf'): "cim.1.activity.ExperimentRelationshipType.continuationOf",
    (activity.ExperimentRelationshipType, 'controlExperiment'): "cim.1.activity.ExperimentRelationshipType.controlExperiment",
    (activity.ExperimentRelationshipType, 'higherResolutionVersionOf'): "cim.1.activity.ExperimentRelationshipType.higherResolutionVersionOf",
    (activity.ExperimentRelationshipType, 'previousRealisation'): "cim.1.activity.ExperimentRelationshipType.previousRealisation",
    (activity.ExperimentRelationshipType, 'lowerResolutionVersionOf'): "cim.1.activity.ExperimentRelationshipType.lowerResolutionVersionOf",
    (activity.ExperimentRelationshipType, 'increaseEnsembleOf'): "cim.1.activity.ExperimentRelationshipType.increaseEnsembleOf",
    (activity.DownscalingType, 'dynamic'): "cim.1.activity.DownscalingType.dynamic",
    (activity.DownscalingType, 'statistical'): "cim.1.activity.DownscalingType.statistical",
    (activity.SimulationType, 'assimilation'): "cim.1.activity.SimulationType.assimilation",
    (activity.SimulationType, 'simulationComposite'): "cim.1.activity.SimulationType.simulationComposite",
    (activity.SimulationType, 'simulationRun'): "cim.1.activity.SimulationType.simulationRun",
    (activity.ConformanceType, 'not conformant'): "cim.1.activity.ConformanceType.not-conformant",
    (activity.ConformanceType, 'standard config'): "cim.1.activity.ConformanceType.standard-config",
    (activity.ConformanceType, 'via inputs'): "cim.1.activity.ConformanceType.via-inputs",
    (activity.ConformanceType, 'via model mods'): "cim.1.activity.ConformanceType.via-model-mods",
    (activity.ConformanceType, 'combination'): "cim.1.activity.ConformanceType.combination",
    (activity.ConformanceType, 'not-xxx'): "cim.1.activity.ConformanceType.not-xxx",
    (activity.SimulationRelationshipType, 'continuationOf'): "cim.1.activity.SimulationRelationshipType.continuationOf",
    (activity.SimulationRelationshipType, 'previousSimulation'): "cim.1.activity.SimulationRelationshipType.previousSimulation",
    (activity.SimulationRelationshipType, 'higherResolutionVersionOf'): "cim.1.activity.SimulationRelationshipType.higherResolutionVersionOf",
    (activity.SimulationRelationshipType, 'lowerResolutionVersionOf'): "cim.1.activity.SimulationRelationshipType.lowerResolutionVersionOf",
    (activity.SimulationRelationshipType, 'fixedVersionOf'): "cim.1.activity.SimulationRelationshipType.fixedVersionOf",
    (activity.SimulationRelationshipType, 'followingSimulation'): "cim.1.activity.SimulationRelationshipType.followingSimulation",
    (activity.SimulationRelationshipType, 'extensionOf'): "cim.1.activity.SimulationRelationshipType.extensionOf",
    (activity.SimulationRelationshipType, 'responseTo'): "cim.1.activity.SimulationRelationshipType.responseTo",
    (software.SpatialRegriddingDimensionType, '1D'): "cim.1.software.SpatialRegriddingDimensionType.1D",
    (software.SpatialRegriddingDimensionType, '2D'): "cim.1.software.SpatialRegriddingDimensionType.2D",
    (software.SpatialRegriddingDimensionType, '3D'): "cim.1.software.SpatialRegriddingDimensionType.3D",
    (software.CouplingFrameworkType, 'ESMF'): "cim.1.software.CouplingFrameworkType.ESMF",
    (software.CouplingFrameworkType, 'BFG'): "cim.1.software.CouplingFrameworkType.BFG",
    (software.CouplingFrameworkType, 'OASIS'): "cim.1.software.CouplingFrameworkType.OASIS",
    (software.SpatialRegriddingStandardMethodType, 'cubic'): "cim.1.software.SpatialRegriddingStandardMethodType.cubic",
    (software.SpatialRegriddingStandardMethodType, 'conservative-first-order'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative-first-order",
    (software.SpatialRegriddingStandardMethodType, 'conservative-second-order'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative-second-order",
    (software.SpatialRegriddingStandardMethodType, 'conservative'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative",
    (software.SpatialRegriddingStandardMethodType, 'non-conservative'): "cim.1.software.SpatialRegriddingStandardMethodType.non-conservative",
    (software.SpatialRegriddingStandardMethodType, 'linear'): "cim.1.software.SpatialRegriddingStandardMethodType.linear",
    (software.SpatialRegriddingStandardMethodType, 'near-neighbour'): "cim.1.software.SpatialRegriddingStandardMethodType.near-neighbour",
    (software.TimingUnits, 'seconds'): "cim.1.software.TimingUnits.seconds",
    (software.TimingUnits, 'minutes'): "cim.1.software.TimingUnits.minutes",
    (software.TimingUnits, 'hours'): "cim.1.software.TimingUnits.hours",
    (software.TimingUnits, 'days'): "cim.1.software.TimingUnits.days",
    (software.TimingUnits, 'months'): "cim.1.software.TimingUnits.months",
    (software.TimingUnits, 'years'): "cim.1.software.TimingUnits.years",
    (software.TimingUnits, 'decades'): "cim.1.software.TimingUnits.decades",
    (software.TimingUnits, 'centuries'): "cim.1.software.TimingUnits.centuries",
    (software.ComponentPropertyIntentType, 'in'): "cim.1.software.ComponentPropertyIntentType.in",
    (software.ComponentPropertyIntentType, 'out'): "cim.1.software.ComponentPropertyIntentType.out",
    (software.ComponentPropertyIntentType, 'inout'): "cim.1.software.ComponentPropertyIntentType.inout",
}
