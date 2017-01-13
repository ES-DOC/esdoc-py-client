# -*- coding: utf-8 -*-

"""
.. module:: model_realm.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Model realm notebook helper.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections
import json
import os

from pyesdoc.mp.specializations import get_model_realm_specialization
from pyesdoc.mp.specializations import get_property_specialization
from pyesdoc.ipython import constants



class NotebookData(object):
    """Model realm ipython data manager.

    """
    def __init__(self, mip_era, institute, source_id, realm):
        """Instance initialiser.

        """
        self.authors = list()
        self.contributors = list()
        self.content = dict()
        self.institute = institute
        self.mip_era = mip_era
        self.prop = None
        self.prop_specialization = None
        self.realm = realm
        self.source_id = source_id
        self.specialization = get_model_realm_specialization(mip_era, realm)


    @property
    def notebook_filename(self):
        """Gets notebook file name.

        """
        return "{}--{}--{}.ipynb".format(self.institute, self.source_id, self.realm)


    @property
    def output_filename(self):
        """Gets output file name.

        """
        return "{}--{}--{}.json".format(self.institute, self.source_id, self.realm)


    def set_author(self, name, email):
        """Adds an author to managed collection.

        """
        # TODO: validate with reg-ex.
        self.authors.append((name, email))


    def set_contributor(self, name, email):
        """Adds a contributor to managed collection.

        """
        # TODO: validate contributor with reg-ex.
        self.contributors.append((name, email))


    def set_id(self, prop_id):
        """Sets id of specialized property being edited.

        """
        self.content[prop_id] = {
            'values': [],
            'qc_status': 0
        }
        self.prop = self.content[prop_id]
        self.prop_specialization = get_property_specialization(prop_id)


    def set_qc_status(self, qc_status):
        """Sets qc-status of specialized property being edited.

        """
        if qc_status not in constants.QC_STATES:
            raise ValueError("Invalid QC status")
        self.prop['qc_status'] = qc_status


    def set_value(self, val):
        """Sets a scalar value.

        """
        # Error if trying to add > 1 value to a property with singular cardinality.
        if not self.prop_specialization.is_collection and \
           len(self.prop['values']) >= 1:
            raise ValueError("Invalid property: only one value can be added")

        # Delegate validation to specialization.
        self.prop_specialization.validate_value(val)

        # Accept value.
        self.prop['values'].append(val)


    def get_values(self, specialization_id):
        """Returns a set of values.

        """
        return self.content.get(specialization_id, dict()).get('values', [])


    def get_qc_status(self, specialization_id):
        """Returns a property qc status.

        """
        return self.content.get(specialization_id, dict()).get('qc_status', 0)


    def read(self, output_dir):
        """Initialises state from previously saved output.

        """
        fpath = os.path.join(output_dir, self.output_filename)
        if os.path.isfile(fpath):
            with open(fpath, 'r') as fstream:
                self._from_dict(json.loads(fstream.read()))


    def write(self, output_dir=None):
        """Persists state to file system.

        """
        if output_dir is None:
            output_dir = os.getcwd()
            output_dir = output_dir.replace('notebooks', 'output')
        output_filepath = os.path.join(output_dir, self.output_filename)
        with open(output_filepath, 'w') as fstream:
            fstream.write(json.dumps(self._to_dict(), indent=4))


    def _from_dict(self, obj):
        """Initialises internal state from a dictionary.

        """
        self.mip_era = obj['MIP_ERA']
        self.institute = obj['INSTITUTE']
        self.source_id = obj['SOURCE_ID']
        self.realm = obj['REALM']
        self.authors = [(i['name'], i['email']) for i in obj['AUTHORS']]
        self.contributors = [(i['name'], i['email']) for i in obj['CONTRIBUTORS']]
        self.content = obj['CONTENT']


    def _to_dict(self):
        """Returns a dictionary representation of internal state.

        """
        obj = collections.OrderedDict()
        obj['MIP_ERA'] = self.mip_era
        obj['INSTITUTE'] = self.institute
        obj['SOURCE_ID'] = self.source_id
        obj['REALM'] = self.realm
        obj['AUTHORS'] = [{'name': i[0], 'email': i[1]} for i in self.authors]
        obj['CONTRIBUTORS'] = [{'name': i[0], 'email': i[1]} for i in self.contributors]
        obj['CONTENT'] = collections.OrderedDict()
        for specialization_id in sorted(self.content.keys()):
            specialization_obj = self.content[specialization_id]
            if specialization_obj['qc_status'] or specialization_obj['values']:
                obj['CONTENT'][specialization_id] = self.content[specialization_id]

        return obj

