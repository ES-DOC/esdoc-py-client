# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_data_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid

import typeset_for_activity_package as activity
import typeset_for_shared_package as shared



class Dataset(object):
    """A concrete class within the cim v2 type system.

    Dataset discovery information.

    """
    def __init__(self):
        """Constructor.

        """
        super(Dataset, self).__init__()

        self.availability = []                            # shared.OnlineResource
        self.description = None                           # unicode
        self.drs_datasets = []                            # drs.DrsPublicationDataset
        self.link_to_produced_by = None                   # shared.DocReference
        self.link_to_responsible_parties = []             # shared.DocReference
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.name = None                                  # unicode
        self.produced_by = None                           # data.Simulation
        self.references = []                              # shared.Citation
        self.related_to_dataset = []                      # data.RelatedData
        self.responsible_parties = []                     # shared.Responsibility


class RelatedData(shared.CimLink):
    """A concrete class within the cim v2 type system.

    A related dataset and a controlled relationship.

    """
    def __init__(self):
        """Constructor.

        """
        super(RelatedData, self).__init__()

        self.link_to_other_dataset = None                 # shared.DocReference
        self.other_dataset = None                         # data.Dataset
        self.relationship = None                          # data.DataAssociationTypes


class Simulation(activity.Activity):
    """A concrete class within the cim v2 type system.

    Simulation class provides the integrating link about what models were run and wny.
    In many cases this should be auto-generated from output file headers.

    """
    def __init__(self):
        """Constructor.

        """
        super(Simulation, self).__init__()

        self.calendar = None                              # shared.Calendar
        self.ensemble_identifier = None                   # unicode
        self.link_to_part_of_project = []                 # shared.DocReference
        self.link_to_primary_ensemble = None              # shared.DocReference
        self.link_to_ran_for_experiments = []             # shared.DocReference
        self.link_to_used = None                          # shared.DocReference
        self.parent_simulation = None                     # activity.ParentSimulation
        self.part_of_project = []                         # designing.Project
        self.primary_ensemble = None                      # activity.Ensemble
        self.ran_for_experiments = []                     # designing.NumericalExperiment
        self.used = None                                  # science.Model


class VariableCollection(object):
    """A concrete class within the cim v2 type system.

    A collection of variables within the scope of a code or process element.

    """
    def __init__(self):
        """Constructor.

        """
        super(VariableCollection, self).__init__()

        self.collection_name = None                       # unicode
        self.variables = []                               # unicode


class Downscaling(Simulation):
    """A concrete class within the cim v2 type system.

    Defines a downscaling activity.

    """
    def __init__(self):
        """Constructor.

        """
        super(Downscaling, self).__init__()

        self.downscaled_from = None                       # data.Simulation
        self.link_to_downscaled_from = None               # shared.DocReference


class DataAssociationTypes(object):
    """An enumeration within the cim v2 type system.

    Set of possible dataset associations.
    Selected from, and extended from,  ISO19115 (2014) DS_AssociationTypeCode.
    """

    pass


