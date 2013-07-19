"""
.. module:: cim.v1.decoding.decoder_for_activity_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.059365.

"""

# Module imports.
from lxml import etree as et

from pyesdoc.serialization.decoder_xml_utils import *
from pyesdoc.ontologies.cim.v1.serialization.decoder_for_data_package import *
from pyesdoc.ontologies.cim.v1.serialization.decoder_for_shared_package import *
from pyesdoc.ontologies.cim.v1.serialization.decoder_for_software_package import *
from pyesdoc.ontologies.cim.v1.types.activity import *




def decode_activity(xml, nsmap):
    """Decodes an instance of the following type: activity.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Activity

    """
    decodings = [
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(Activity(), xml, nsmap, decodings)


def decode_boundary_condition(xml, nsmap):
    """Decodes an instance of the following type: boundary condition.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.BoundaryCondition

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('id', False, 'str', 'child::cim:id'),
        ('name', False, 'str', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source_reference', False, decode_cim_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(BoundaryCondition(), xml, nsmap, decodings)


def decode_conformance(xml, nsmap):
    """Decodes an instance of the following type: conformance.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Conformance

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('frequency', False, 'str', 'child::cim:frequency'),
        ('is_conformant', False, 'bool', '@conformant'),
        ('requirements', True, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirements', True, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('requirements_references', True, decode_cim_reference, 'child::cim:requirement/cim:reference'),
        ('sources', True, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('sources', True, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('sources', True, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('sources', True, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources_references', True, decode_cim_reference, 'child::cim:source/cim:reference'),
        ('type', False, 'str', '@type'),
    ]

    return set_attributes(Conformance(), xml, nsmap, decodings)


def decode_downscaling_simulation(xml, nsmap):
    """Decodes an instance of the following type: downscaling simulation.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DownscalingSimulation

    """
    decodings = [
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('cim_info', False, decode_cim_info, 'self::cim:downscalingSimulation'),
        ('description', False, 'str', 'child::cim:description'),
        ('downscaled_from', False, decode_data_object, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:dataObject'),
        ('downscaled_from', False, decode_data_content, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:dataContent'),
        ('downscaled_from', False, decode_component_property, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:componentProperty'),
        ('downscaled_from', False, decode_model_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaled_from', False, decode_processor_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaled_from', False, decode_statistical_model_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaled_from_reference', False, decode_cim_reference, 'child::cim:downscaledFrom/cim:reference'),
        ('downscaling_id', False, 'str', 'child::cim:downscalingID'),
        ('downscaling_type', False, 'str', 'self::cim:downscalingSimulation/@downscalingType'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('outputs', True, decode_data_object, 'child::cim:output/cim:dataObject'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('supports_references', True, decode_cim_reference, 'child::cim:supports/cim:reference'),
    ]

    return set_attributes(DownscalingSimulation(), xml, nsmap, decodings)


def decode_ensemble(xml, nsmap):
    """Decodes an instance of the following type: ensemble.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Ensemble

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:ensemble'),
        ('description', False, 'str', 'child::cim:description'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('members', True, decode_ensemble_member, 'child::cim:ensembleMember'),
        ('outputs', True, decode_data_object, 'child::cim:output/cim:output/cim:dataObject'),
        ('outputs', True, decode_data_content, 'child::cim:output/cim:output/cim:dataContent'),
        ('outputs', True, decode_component_property, 'child::cim:output/cim:output/cim:componentProperty'),
        ('outputs', True, decode_model_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('outputs', True, decode_processor_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('outputs', True, decode_statistical_model_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('outputs_references', True, decode_cim_reference, 'child::cim:output/cim:reference'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('supports_references', True, decode_cim_reference, 'child::cim:supports/cim:reference'),
        ('types', True, 'str', 'child::cim:ensembleType/@value'),
    ]

    return set_attributes(Ensemble(), xml, nsmap, decodings)


def decode_ensemble_member(xml, nsmap):
    """Decodes an instance of the following type: ensemble member.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.EnsembleMember

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('ensemble', False, decode_ensemble, 'child::cim:ensemble/cim:ensemble'),
        ('ensemble_ids', True, decode_standard_name, 'child::cim:ensembleMemberID'),
        ('ensemble_reference', False, decode_cim_reference, 'child::cim:ensemble/cim:reference'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('simulation', False, decode_simulation, 'child::cim:ensemble/cim:simulation'),
        ('simulation_reference', False, decode_cim_reference, 'child::cim:simulation/cim:reference'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('supports_references', True, decode_cim_reference, 'child::cim:supports/cim:reference'),
    ]

    return set_attributes(EnsembleMember(), xml, nsmap, decodings)


def decode_experiment(xml, nsmap):
    """Decodes an instance of the following type: experiment.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Experiment

    """
    decodings = [
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(Experiment(), xml, nsmap, decodings)


def decode_experiment_relationship(xml, nsmap):
    """Decodes an instance of the following type: experiment relationship.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.ExperimentRelationship

    """
    decodings = [
    ]

    return set_attributes(ExperimentRelationship(), xml, nsmap, decodings)


def decode_experiment_relationship_target(xml, nsmap):
    """Decodes an instance of the following type: experiment relationship target.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.ExperimentRelationshipTarget

    """
    decodings = [
    ]

    return set_attributes(ExperimentRelationshipTarget(), xml, nsmap, decodings)


def decode_initial_condition(xml, nsmap):
    """Decodes an instance of the following type: initial condition.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.InitialCondition

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('id', False, 'str', 'child::cim:id'),
        ('name', False, 'str', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source_reference', False, decode_cim_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(InitialCondition(), xml, nsmap, decodings)


def decode_lateral_boundary_condition(xml, nsmap):
    """Decodes an instance of the following type: lateral boundary condition.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.LateralBoundaryCondition

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('id', False, 'str', 'child::cim:id'),
        ('name', False, 'str', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source_reference', False, decode_cim_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(LateralBoundaryCondition(), xml, nsmap, decodings)


def decode_measurement_campaign(xml, nsmap):
    """Decodes an instance of the following type: measurement campaign.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.MeasurementCampaign

    """
    decodings = [
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(MeasurementCampaign(), xml, nsmap, decodings)


def decode_numerical_activity(xml, nsmap):
    """Decodes an instance of the following type: numerical activity.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.NumericalActivity

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('supports_references', True, decode_cim_reference, 'child::cim:supports/cim:reference'),
    ]

    return set_attributes(NumericalActivity(), xml, nsmap, decodings)


def decode_numerical_experiment(xml, nsmap):
    """Decodes an instance of the following type: numerical experiment.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.NumericalExperiment

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:numericalExperiment'),
        ('description', False, 'str', 'child::cim:description'),
        ('experiment_id', False, 'str', 'child::cim:experimentID'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('requirements', True, decode_initial_condition, 'child::cim:numericalRequirement/cim:initialCondition'),
        ('requirements', True, decode_boundary_condition, 'child::cim:numericalRequirement/cim:boundaryCondition'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:numericalRequirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:numericalRequirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_output_requirement, 'child::cim:numericalRequirement/cim:outputRequirement'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
    ]

    return set_attributes(NumericalExperiment(), xml, nsmap, decodings)


def decode_numerical_requirement(xml, nsmap):
    """Decodes an instance of the following type: numerical requirement.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.NumericalRequirement

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('id', False, 'str', 'child::cim:id'),
        ('name', False, 'str', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source_reference', False, decode_cim_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(NumericalRequirement(), xml, nsmap, decodings)


def decode_numerical_requirement_option(xml, nsmap):
    """Decodes an instance of the following type: numerical requirement option.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.NumericalRequirementOption

    """
    decodings = [
        ('relationship', False, 'str', 'self::cim:requirementOption/@optionRelationship'),
        ('requirement', False, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirement', False, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('requirement', False, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('requirement', False, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirement', False, decode_lateral_boundary_condition, 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition'),
    ]

    return set_attributes(NumericalRequirementOption(), xml, nsmap, decodings)


def decode_output_requirement(xml, nsmap):
    """Decodes an instance of the following type: output requirement.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.OutputRequirement

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('id', False, 'str', 'child::cim:id'),
        ('name', False, 'str', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source_reference', False, decode_cim_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(OutputRequirement(), xml, nsmap, decodings)


def decode_physical_modification(xml, nsmap):
    """Decodes an instance of the following type: physical modification.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.PhysicalModification

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('frequency', False, 'str', 'child::cim:frequency'),
        ('is_conformant', False, 'bool', '@conformant'),
        ('requirements', True, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirements', True, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('requirements_references', True, decode_cim_reference, 'child::cim:requirement/cim:reference'),
        ('sources', True, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('sources', True, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('sources', True, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('sources', True, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources_references', True, decode_cim_reference, 'child::cim:source/cim:reference'),
        ('type', False, 'str', '@type'),
    ]

    return set_attributes(PhysicalModification(), xml, nsmap, decodings)


def decode_simulation(xml, nsmap):
    """Decodes an instance of the following type: simulation.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Simulation

    """
    decodings = [
        ('authors', False, 'str', 'child::cim:authorsList/cim:list'),
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('control_simulation_reference', False, decode_cim_reference, 'child::cim:controlSimulation/cim:reference'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('description', False, 'str', 'child::cim:description'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('simulation_id', False, 'str', 'child::cim:simulationID'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('supports_references', True, decode_cim_reference, 'child::cim:supports/cim:reference'),
    ]

    return set_attributes(Simulation(), xml, nsmap, decodings)


def decode_simulation_composite(xml, nsmap):
    """Decodes an instance of the following type: simulation composite.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.SimulationComposite

    """
    decodings = [
        ('authors', False, 'str', 'child::cim:authorsList/cim:list'),
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('child', True, decode_simulation_run, 'child::cim:child'),
        ('child', True, decode_simulation_composite, 'child::cim:child'),
        ('cim_info', False, decode_cim_info, 'self::cim:simulationRun'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('control_simulation_reference', False, decode_cim_reference, 'child::cim:controlSimulation/cim:reference'),
        ('date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:dateRange/cim:openDateRange'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('description', False, 'str', 'child::cim:description'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rank', False, 'int', 'child::cim:rank'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('simulation_id', False, 'str', 'child::cim:simulationID'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('supports_references', True, decode_cim_reference, 'child::cim:supports/cim:reference'),
    ]

    return set_attributes(SimulationComposite(), xml, nsmap, decodings)


def decode_simulation_relationship(xml, nsmap):
    """Decodes an instance of the following type: simulation relationship.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.SimulationRelationship

    """
    decodings = [
    ]

    return set_attributes(SimulationRelationship(), xml, nsmap, decodings)


def decode_simulation_relationship_target(xml, nsmap):
    """Decodes an instance of the following type: simulation relationship target.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.SimulationRelationshipTarget

    """
    decodings = [
    ]

    return set_attributes(SimulationRelationshipTarget(), xml, nsmap, decodings)


def decode_simulation_run(xml, nsmap):
    """Decodes an instance of the following type: simulation run.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.SimulationRun

    """
    decodings = [
        ('authors', False, 'str', 'child::cim:authorsList/cim:list'),
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('cim_info', False, decode_cim_info, 'self::cim:simulationRun'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('control_simulation_reference', False, decode_cim_reference, 'child::cim:controlSimulation/cim:reference'),
        ('date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:dateRange/cim:openDateRange'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('description', False, 'str', 'child::cim:description'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('model', False, decode_model_component, 'child::cim:model/cim:modelComponent'),
        ('model_reference', False, decode_cim_reference, 'child::cim:model/cim:reference'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('simulation_id', False, 'str', 'child::cim:simulationID'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('supports_references', True, decode_cim_reference, 'child::cim:supports/cim:reference'),
    ]

    return set_attributes(SimulationRun(), xml, nsmap, decodings)


def decode_spatio_temporal_constraint(xml, nsmap):
    """Decodes an instance of the following type: spatio temporal constraint.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.SpatioTemporalConstraint

    """
    decodings = [
        ('date_range', False, decode_closed_date_range, 'child::cim:requiredDuration/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:requiredDuration/cim:openDateRange'),
        ('description', False, 'str', 'child::cim:description'),
        ('id', False, 'str', 'child::cim:id'),
        ('name', False, 'str', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source_reference', False, decode_cim_reference, 'child::cim:source/cim:reference'),
        ('spatial_resolution', False, 'str', 'child::cim:spatialResolution'),
    ]

    return set_attributes(SpatioTemporalConstraint(), xml, nsmap, decodings)


