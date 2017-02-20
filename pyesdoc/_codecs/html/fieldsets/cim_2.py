# -*- coding: utf-8 -*-

"""
.. module:: cim_1.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: CIM v1 HTML field sets.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import collections

from pyesdoc._codecs.html.fieldsets.field import Field
from pyesdoc.ontologies import cim



_SEPARATOR = "  |  "

# Experimental relationship types and their labels.
_EXPERIMENTAL_RELATIONSHIP_LABELS = [
    ("is_initialized_by", "Parent"),
    ("is_sibling_of", "Siblings"),
    ("is_initializer_of", "Children"),
    ("is_perturbation_from", "Control"),
    ("is_control_for", "Provides control to"),
    ("is_constrained_by", "Boundary Conditions From"),
    ("is_constrainer_of", "Provides constraints to"),
]


def _get_related_experiments(e, r_type):
    result = []
    for i in sorted(e.related_experiments, key=lambda i: i.name):
        if i.relationship == r_type:
            result.append((i.name, i.viewer_url))

    return result


def _get_designing_project_overview(p):
    """Returns a dynamically constructed fieldset.

    """
    fields = [
        Field('Name', path='name'),
        Field('Long Name', path='long_name'),
        Field('Homepage', path='homepage'),
        Field('Description', path='description'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(','))),
        Field('Rationale', path='rationale'),
        Field('Objectives', path='objectives')
    ]

    # Associated sub-projects.
    if p.sub_projects:
        fields.append(Field('Sub Projects',
            link_factory=lambda p: [(i.name, i.viewer_url) for i in p.sub_projects])
        )

    # Governed experiments by tier.
    for tier in sorted(p.ext.tiered_experiments):
        experiments = p.ext.tiered_experiments[tier]
        description = "Tier {} Experiments".format(tier)
        fields.append(Field(description,
            link_factory=[(i.name, i.viewer_url) for i in experiments])
        )

    # Other experiments.
    if p.ext.other_experiments:
        fields.append(Field('Other Experiments',
            link_factory=lambda p: [(i.name, i.viewer_url) for i in p.ext.other_experiments])
            )

    return fields


def _get_designing_numericalexperiment_relationships(e):
    """Returns a dynamically constructed fieldset.

    """
    fields = []
    for typeof, label in _EXPERIMENTAL_RELATIONSHIP_LABELS:
        if [i for i in e.related_experiments if i.relationship == typeof]:
            fields.append(Field(label, link_factory=_get_related_experiments(e, typeof)))

    return fields


# Document field sets.
FIELDSETS = {
    'cim.2.designing.numericalexperiment-overview': [
        Field('MIP Era', path='meta.project'),
        Field('Related MIPs',
            link_factory=lambda v: [(i.name, i.viewer_url) for i in sorted(v.related_mips, key=lambda v: v.name)]
            ),
        Field('Institute', path='meta.institute'),
        Field('Canonical Name', path='canonical_name'),
        Field('Alternative Names', path='alternative_names',
            input_formatter=lambda v: _SEPARATOR.join(v)
            ),
        Field('Long Name', path='long_name'),
        Field('Tier', path='tier'),
        Field('Description', path='description'),
        Field('Rationale', path='rationale'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(','))
            )
    ],

    'cim.2.designing.numericalexperiment-relationships':
        _get_designing_numericalexperiment_relationships,

    str(cim.v2.designing.EnsembleRequirement) : [
        Field('Name', path='canonical_name'),
        Field('Description', path='description'),
        Field('Ensemble Type', path='ensemble_type'),
        Field('Minimum Size', path='minimum_size'),
        Field('Conformance Requested ?', path='is_conformance_requested'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(','))
            )
    ],

    str(cim.v2.designing.ForcingConstraint) : [
        Field('Name', path='canonical_name'),
        Field('Description', path='description'),
        Field('Rationale', path='rationale'),
        Field('Forcing Type', path='forcing_type', capitalize_value=True),
        Field('Conformance Requested ?', path='is_conformance_requested'),
        Field('Scope', path='scope', capitalize_value=True),
        Field('Data Link', path='data_link.name',
            link_path=lambda v: v.data_link.availability[0].linkage,
            predicate=lambda v: v.data_link is not None and \
                                len(v.data_link.availability) > 0
            ),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(','))
            )
    ],

    str(cim.v2.designing.MultiEnsemble) : [
        Field('Name', path='canonical_name'),
        Field('Description', path='description'),
        Field('Forcing Type', path='forcing_type'),
        Field('Conformance Requested ?', path='is_conformance_requested'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(','))
            )
    ],

    str(cim.v2.designing.NumericalRequirement) : [
        Field('Name', path='canonical_name'),
        Field('Description', path='description'),
        Field('Ensemble Type', path='ensemble_type'),
        Field('Minimum Size', path='minimum_size'),
        Field('Conformance Requested ?', path='is_conformance_requested'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(','))
            )
    ],

    str(cim.v2.designing.TemporalConstraint) : [
        Field('Start Date', path='start_date.value'),
        Field('Required Duration', path='required_duration',
            input_formatter=lambda v: "{} {}".format(v.length, v.units)
            ),
        Field('Description', path='description'),
        Field('Conformance Requested ?', path='is_conformance_requested'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(','))
            )
    ],

    'cim.2.designing.project-overview':
        _get_designing_project_overview,

    'cim.2.shared.citation' : [
        Field('DOI', path='doi',
            link_path=lambda v: "https://doi.org/{}".format(v.doi)
            ),
        Field('Title', path='citation_detail', link_path="url.linkage"),
        Field('Context', path='context'),
        Field('Abstract', path='abstract')
    ],

    'cim.2.shared.party' : [
        Field('Name', path='name', link_path="url.linkage"),
        Field('Address', path='address'),
        Field('Email', path='email', email_path='email')
    ]
}
