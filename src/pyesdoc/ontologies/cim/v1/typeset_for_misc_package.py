"""
.. module:: cim.v1.typeset_for_misc_package.py

   :copyright: @2014 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.misc package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2014-01-31 14:14:51.563427.

"""
# Module imports.
import abc
import datetime
import uuid

import typeset_for_shared_package as shared




class DocumentSet(object):
    """A concrete class within the cim v1 type system.

    Encapsulates a set of documents.
    """
    def __init__(self):
        """Constructor.

        """
        super(DocumentSet, self).__init__()

        self.data = []                                    # data.DataObject
        self.doc_info = shared.DocInfo()                  # shared.DocInfo
        self.ensembles = []                               # activity.Ensemble
        self.experiment = None                            # activity.NumericalExperiment
        self.grid = None                                  # grids.GridSpec
        self.model = None                                 # software.ModelComponent
        self.platform = None                              # shared.Platform
        self.simulation = None                            # activity.SimulationRun

