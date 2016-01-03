# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_science_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.science package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared
import typeset_for_software_package as software



class Algorithm(object):
    """A concrete class within the cim v2 type system.

    Used to hold information associated with an algorithm which implements some key
    part of a process. In most cases this is quite a high level concept and isn't intended
    to describe the gory detail of how the code implements the algorithm rather the key
    scientific aspects of the algorithm. In particular, it provides a method
    of grouping variables which take part in an algorithm within a process.

    """
    def __init__(self):
        """Constructor.

        """
        super(Algorithm, self).__init__()

        self.diagnostic_variables = []                    # data.VariableCollection (0.N)
        self.heading = None                               # unicode (1.1)
        self.implementation_overview = None               # unicode (1.1)
        self.prognostic_variables = []                    # data.VariableCollection (0.N)
        self.references = []                              # shared.Citation (0.N)


class ConservationProperties(object):
    """A concrete class within the cim v2 type system.

    Describes how prognostic variables are conserved.

    """
    def __init__(self):
        """Constructor.

        """
        super(ConservationProperties, self).__init__()

        self.corrected_conserved_prognostic_variables = None# data.VariableCollection (0.1)
        self.correction_methodology = None                # unicode (0.1)
        self.flux_correction_was_used = None              # bool (1.1)


class Extent(object):
    """A concrete class within the cim v2 type system.

    Key scientific characteristics of the grid use to simulate a specific domain.
    Note that the extent does not itself describe a grid, so, for example, a polar
    stereographic grid may have an extent of northern boundary 90N, southern boundary
    45N, but the fact that it is PS comes from the grid_type.

    """
    def __init__(self):
        """Constructor.

        """
        super(Extent, self).__init__()

        self.eastern_boundary = None                      # float (0.1)
        self.is_global = None                             # bool (1.1)
        self.maximum_vertical_level = None                # float (0.1)
        self.minimum_vertical_level = None                # float (0.1)
        self.northern_boundary = None                     # float (0.1)
        self.region_known_as = []                         # unicode (0.N)
        self.southern_boundary = None                     # float (0.1)
        self.western_boundary = None                      # float (0.1)
        self.z_units = None                               # unicode (1.1)


class GridSummary(object):
    """A concrete class within the cim v2 type system.

    Key scientific characteristics of the grid use to simulate a specific domain.

    """
    def __init__(self):
        """Constructor.

        """
        super(GridSummary, self).__init__()

        self.grid_extent = None                           # science.Extent (1.1)
        self.grid_layout = None                           # science.GridLayouts (1.1)
        self.grid_type = None                             # science.GridTypes (1.1)


class Model(software.ComponentBase):
    """A concrete class within the cim v2 type system.

    A model component: can be executed standalone, and has as scientific
    description available via a link to a science.domain document. (A configured model can
     be understood in terms of a simulation, a model, and a configuration.).

    """
    def __init__(self):
        """Constructor.

        """
        super(Model, self).__init__()

        self.category = None                              # science.ModelTypes (1.1)
        self.coupled_software_components = []             # science.Model (0.N)
        self.coupler = None                               # software.CouplingFramework (0.1)
        self.extra_conservation_properties = None         # science.ConservationProperties (0.1)
        self.internal_software_components = []            # software.SoftwareComponent (0.N)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.scientific_domain = []                       # science.ScientificDomain (0.N)


class Process(object):
    """A concrete class within the cim v2 type system.

    Provides structure for description of a process simulated within a particular
    area (or domain/realm/component) of a model. This will often be subclassed
    within a specific implementation so that constraints can be used to ensure
    that the process details requested are consistent with project requirements
    for information.

    """
    def __init__(self):
        """Constructor.

        """
        super(Process, self).__init__()

        self.algorithms = []                              # science.Algorithm (0.N)
        self.description = None                           # unicode (0.1)
        self.implementation_overview = None               # unicode (1.1)
        self.keywords = None                              # unicode (1.1)
        self.name = None                                  # unicode (1.1)
        self.properties = []                              # science.ProcessDetail (0.N)
        self.references = []                              # shared.Reference (0.N)
        self.sub_processes = []                           # science.SubProcess (0.N)
        self.time_step_in_process = None                  # float (0.1)


class ProcessDetail(object):
    """A concrete class within the cim v2 type system.

    Provides detail of specific properties of a process, there are two possible specialisations
    expected: (1) A detail_vocabulary is identified, and a cardinality is assigned to that
    for possible responses, or (2) Process_Detail is used to provide a collection for a set of
    properties which are defined in the sub-class. However, those properties must have a type
    which is selected from the classmap (that is, standard 'non-es-doc' types).

    """
    def __init__(self):
        """Constructor.

        """
        super(ProcessDetail, self).__init__()

        self.cardinality_of_selection = None              # science.SelectionCardinality (0.1)
        self.content = None                               # unicode (0.1)
        self.detail_selection = []                        # unicode (0.N)
        self.detail_vocabulary = None                     # unicode (0.1)
        self.heading = None                               # unicode (0.1)


class Resolution(object):
    """A concrete class within the cim v2 type system.

    Describes the computational spatial resolution of a component or process. Not intended
        to replace or replicate the output grid description.  When it appears as part of a process
        description, provide only properties that differ from parent domain. Note that where
        different variables have different grids, differences in resolution can be captured by
        repeating the number_of_ properties.

    """
    def __init__(self):
        """Constructor.

        """
        super(Resolution, self).__init__()

        self.equivalent_horizontal_resolution = None      # float (1.1)
        self.is_adaptive_grid = None                      # bool (0.1)
        self.name = None                                  # unicode (1.1)
        self.number_of_levels = []                        # int (0.N)
        self.number_of_xy_gridpoints = []                 # int (0.N)


class ScientificDomain(object):
    """A concrete class within the cim v2 type system.

    Scientific area of a numerical model - usually a sub-model or component.
    Can also be known as a realm.

    """
    def __init__(self):
        """Constructor.

        """
        super(ScientificDomain, self).__init__()

        self.extra_conservation_properties = None         # science.ConservationProperties (0.1)
        self.grid = None                                  # science.GridSummary (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (1.1)
        self.overview = None                              # unicode (0.1)
        self.realm = None                                 # unicode (0.1)
        self.references = []                              # shared.Reference (0.N)
        self.resolution = None                            # science.Resolution (1.1)
        self.simulates = []                               # science.Process (1.N)
        self.time_step = None                             # float (1.1)
        self.tuning_applied = None                        # science.Tuning (0.1)


class SubProcess(object):
    """A concrete class within the cim v2 type system.

    Provides structure for description of part of process simulated within a particular
    area (or domain/realm/component) of a model. Typically this will be a part of process
    which shares common properties. It will normally be sub classed within a specific
    implementation so that constraints can be used to ensure that the process details requested are
    consistent with projects requirements for information.

    """
    def __init__(self):
        """Constructor.

        """
        super(SubProcess, self).__init__()

        self.description = None                           # unicode (0.1)
        self.implementation_overview = None               # unicode (0.1)
        self.keywords = None                              # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.properties = []                              # science.ProcessDetail (0.N)
        self.references = []                              # shared.Reference (0.N)


class Tuning(object):
    """A concrete class within the cim v2 type system.

    Method used to optimise equation parameters in model component (aka 'tuning').

    """
    def __init__(self):
        """Constructor.

        """
        super(Tuning, self).__init__()

        self.description = None                           # unicode (1.1)
        self.global_mean_metrics_used = None              # data.VariableCollection (0.1)
        self.regional_metrics_used = None                 # data.VariableCollection (0.1)
        self.trend_metrics_used = None                    # data.VariableCollection (0.1)


class GridLayouts(object):
    """An enumeration within the cim v2 type system.

    Defines the set of grid layouts (e.g. Arakawa C-Grid) which are understood.
    """
    is_open = False
    members = [
        "Arakawa-C"
        ]


class GridTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the set of grid types (e.g Cubed Sphere) which are understood.
    """
    is_open = False
    members = [
        "Cubed-Sphere",
        "LatLon",
        "Spectral-Gaussian"
        ]


class ModelTypes(object):
    """An enumeration within the cim v2 type system.

    Defines a set of gross model classes.
    """
    is_open = False
    members = [
        "Atm Only",
        "GCM",
        "GCM-MLO",
        "IGCM",
        "Mesoscale",
        "Ocean Only",
        "Planetary",
        "Process",
        "Regional"
        ]


class SelectionCardinality(object):
    """An enumeration within the cim v2 type system.

    Provides the possible cardinalities for selecting from a controlled vocabulary.
    """
    is_open = False
    members = [
        "0.1",
        "0.N",
        "1.1",
        "1.N"
        ]


