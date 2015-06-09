# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_data_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 14:48:44.254031.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class Dataset(object):
    """A concrete class within the cim v2 type system.

    Discovery level metadata for a dataset.

    """
    def __init__(self):
        """Constructor.

        """
        super(Dataset, self).__init__()

        self.description = None                           # str
        self.references = []                              # shared.Citation
        self.dataset_author = []                          # linked_to(shared.Party)
        self.meta = shared.Meta()                         # shared.Meta
        self.name = None                                  # str
        self.related_to_dataset = []                      # linked_to(data.Dataset)
        self.produced_by = None                           # linked_to(activity.Simulation)
        self.availability = []                            # shared.OnlineResource


