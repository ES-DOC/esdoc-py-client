# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_shared_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.shared package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import abc
import datetime
import uuid




class Cimtext(object):
    """A concrete class within the cim v2 type system.

    Provides a text class which supports plaintext, html, and
    friends (or will do).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Cimtext, self).__init__()

        self.content = None                               # unicode (1.1)
        self.content_type = None                          # shared.TextCode (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.content)


class Citation(object):
    """A concrete class within the cim v2 type system.

    An academic reference to published work.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Citation, self).__init__()

        self.abstract = None                              # unicode (0.1)
        self.citation_detail = None                       # unicode (0.1)
        self.collective_title = None                      # unicode (0.1)
        self.context = None                               # unicode (0.1)
        self.doi = None                                   # unicode (0.1)
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo (1.1)
        self.title = None                                 # unicode (0.1)
        self.type = None                                  # unicode (0.1)
        self.url = None                                   # shared.OnlineResource (0.1)


class DocMetaInfo(object):
    """A concrete class within the cim v2 type system.

    Encapsulates document meta information used by es-doc machinery. Will not normally be
    populated by humans. May duplicate information held in 'visible' metadata.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DocMetaInfo, self).__init__()

        self.author = None                                # shared.Party (0.1)
        self.create_date = None                           # datetime.datetime (1.1)
        self.drs_keys = []                                # unicode (0.N)
        self.drs_path = None                              # unicode (0.1)
        self.external_ids = []                            # unicode (0.N)
        self.id = None                                    # unicode (1.1)
        self.institute = None                             # unicode (0.1)
        self.language = None                              # unicode (1.1)
        self.project = None                               # unicode (1.1)
        self.sort_key = None                              # unicode (0.1)
        self.source = None                                # unicode (1.1)
        self.source_key = None                            # unicode (0.1)
        self.sub_projects = []                            # unicode (0.N)
        self.type = None                                  # unicode (1.1)
        self.type_display_name = None                     # unicode (0.1)
        self.type_sort_key = None                         # unicode (0.1)
        self.update_date = None                           # datetime.datetime (1.1)
        self.version = None                               # int (1.1)


class ExtraAttribute(object):
    """A concrete class within the cim v2 type system.

    An extra attribute with key and value needed to encode further information
    not in the CIM2 domain model or specialisation. Typical use case: in parsing
    data and encoding attributes found in data.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ExtraAttribute, self).__init__()

        self.doc = None                                   # unicode (0.1)
        self.key = None                                   # unicode (1.1)
        self.type = None                                  # unicode (0.1)
        self.value = None                                 # unicode (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}:{}".format(self.key, self.value)


class OnlineResource(object):
    """A concrete class within the cim v2 type system.

    A minimal approximation of ISO19115 CI_ONLINERESOURCE, provides a link and details
    of how to use that link.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(OnlineResource, self).__init__()

        self.description = None                           # unicode (0.1)
        self.linkage = None                               # unicode (1.1)
        self.name = None                                  # unicode (1.1)
        self.protocol = None                              # unicode (0.1)


class Party(object):
    """A concrete class within the cim v2 type system.

    Implements minimal material for an ISO19115-1 (2014) compliant party.
    For our purposes this is a much better animal than the previous responsibleParty 
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Party, self).__init__()

        self.address = None                               # unicode (0.1)
        self.email = None                                 # unicode (0.1)
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (0.1)
        self.orcid_id = None                              # unicode (0.1)
        self.organisation = None                          # bool (0.1)
        self.url = None                                   # shared.OnlineResource (0.1)


class QualityReview(object):
    """A concrete class within the cim v2 type system.

    Assertions as to the completeness and quality of a document.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(QualityReview, self).__init__()

        self.date = None                                  # unicode (1.1)
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo (1.1)
        self.metadata_reviewer = None                     # shared.Party (1.1)
        self.quality_description = None                   # unicode (1.1)
        self.quality_status = None                        # shared.QualityStatus (0.1)
        self.target_document = None                       # shared.DocReference (1.1)


class Responsibility(object):
    """A concrete class within the cim v2 type system.

    Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty). Combines a person and their role in doing something.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Responsibility, self).__init__()

        self.party = []                                   # shared.Party (1.N)
        self.role = None                                  # shared.RoleCode (1.1)
        self.when = None                                  # time.TimePeriod (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}:{}".format(self.role, self.party)


class DocReference(OnlineResource):
    """A concrete class within the cim v2 type system.

    Specialisation of online resource for link between CIM documents, whether the
    remote document exists when complete, or not.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DocReference, self).__init__()

        self.constraint_vocabulary = None                 # unicode (0.1)
        self.context = None                               # unicode (0.1)
        self.id = None                                    # unicode (0.1)
        self.relationship = None                          # unicode (0.1)
        self.type = None                                  # unicode (1.1)
        self.version = None                               # int (0.1)


class DocumentTypes(object):
    """An enumeration within the cim v2 type system.

    The complete set of CIM document types, that is, all classes which carry the
    document metadata attributes.
    """
    is_open = False
    members = [
        "Conformance",
        "Dataset",
        "DomainProperties",
        "Downscaling",
        "Ensemble",
        "EnsembleRequirement",
        "ExternalDocument",
        "ForcingConstraint",
        "Grid",
        "Machine",
        "Model",
        "MultiEnsemble",
        "MultiTimeEnsemble",
        "NumericalExperiment",
        "NumericalRequirement",
        "OutputTemporalRequirement",
        "Party",
        "Performance",
        "Project",
        "QualityReview",
        "ScientificDomain",
        "Simulation",
        "SimulationPlan",
        "TemporalConstraint",
        "UberEnsemble"
        ]


class NilReason(object):
    """An enumeration within the cim v2 type system.

    Provides an enumeration of possible reasons why a property has not been defined
    Based on GML nilReason as discussed here: https://www.seegrid.csiro.au/wiki/AppSchemas/NilValues.
    """
    is_open = False
    members = [
        "nil:inapplicable",
        "nil:missing",
        "nil:template",
        "nil:unknown",
        "nil:withheld"
        ]


class QualityStatus(object):
    """An enumeration within the cim v2 type system.

    Assertion as to the review status of document.
    """
    is_open = False
    members = [
        "finalised",
        "incomplete",
        "reviewed",
        "under_review"
        ]


class RoleCode(object):
    """An enumeration within the cim v2 type system.

    Responsibility role codes: roles that a party may play in delivering a responsibility.
    """
    is_open = False
    members = [
        "Principal Investigator",
        "author",
        "collaborator",
        "custodian",
        "distributor",
        "metadata_author",
        "metadata_reviewer",
        "originator",
        "owner",
        "point of contact",
        "processor",
        "publisher",
        "resource provider",
        "sponsor",
        "user"
        ]


class TextCode(object):
    """An enumeration within the cim v2 type system.

    Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.
    """
    is_open = False
    members = [
        "plaintext"
        ]


