# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_shared_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.shared package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid




class Calendar(object):
    """A concrete class within the cim v2 type system.

    Describes the calendar required/used in an experiment/simulation.
    This class is based on the calendar attributes and properties found in the
    CF netCDF conventions.

    """
    def __init__(self):
        """Constructor.

        """
        super(Calendar, self).__init__()

        self.description = None                           # unicode
        self.month_lengths = []                           # int
        self.name = None                                  # unicode
        self.standard_name = None                         # shared.CalendarTypes


class Cimtext(object):
    """A concrete class within the cim v2 type system.

    Provides a text class which supports plaintext, html, and
    friends (or will do).

    """
    def __init__(self):
        """Constructor.

        """
        super(Cimtext, self).__init__()

        self.content = None                               # unicode
        self.content_type = None                          # shared.TextCode


class Citation(object):
    """A concrete class within the cim v2 type system.

    Description of material suitable for citation - in the academic sense, i.e. for a journal bibliography.

    """
    def __init__(self):
        """Constructor.

        """
        super(Citation, self).__init__()

        self.abstract = None                              # unicode
        self.citation_str = None                          # unicode
        self.context = None                               # unicode
        self.doi = None                                   # unicode
        self.short_cite = None                            # unicode
        self.title = None                                 # unicode
        self.url = None                                   # shared.OnlineResource


class DateTime(object):
    """A concrete class within the cim v2 type system.

    A date or time. Either in simulation time with the simulation
    calendar, or with reference to a simulation start, in which
    case the datetime is an interval after the start date.

    """
    def __init__(self):
        """Constructor.

        """
        super(DateTime, self).__init__()

        self.offset = None                                # bool
        self.value = None                                 # unicode


class DatetimeSet(object):
    """An abstract class within the cim v2 type system.

    Base class for a set of dates or times.
    Note that we assume either a periodic set of dates which can
    be date and/or time, or an irregular set which can only be dates.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DatetimeSet, self).__init__()

        self.length = None                                # int


class DocMetaInfo(object):
    """A concrete class within the cim v2 type system.

    Encapsulates document meta information.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocMetaInfo, self).__init__()

        self.author = None                                # shared.Party
        self.author_reference = None                      # shared.DocReference
        self.create_date = None                           # datetime.datetime
        self.drs_keys = []                                # unicode
        self.drs_path = None                              # unicode
        self.external_ids = []                            # unicode
        self.id = None                                    # uuid.UUID
        self.institute = None                             # unicode
        self.language = None                              # unicode
        self.project = None                               # unicode
        self.sort_key = None                              # unicode
        self.source = None                                # unicode
        self.source_key = None                            # unicode
        self.type = None                                  # unicode
        self.type_display_name = None                     # unicode
        self.type_sort_key = None                         # unicode
        self.update_date = None                           # datetime.datetime
        self.version = None                               # int


class DocReference(object):
    """A concrete class within the cim v2 type system.

    A reference to another cim entity.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocReference, self).__init__()

        self.description = None                           # unicode
        self.id = None                                    # uuid.UUID
        self.name = None                                  # unicode
        self.type = None                                  # unicode
        self.url = None                                   # unicode
        self.version = None                               # int


class KeyFloat(object):
    """A concrete class within the cim v2 type system.

    Holds a key and a float value.

    """
    def __init__(self):
        """Constructor.

        """
        super(KeyFloat, self).__init__()

        self.key = None                                   # unicode
        self.value = None                                 # float


class NumberArray(object):
    """A concrete class within the cim v2 type system.

    Provides a class for entering an array of numbers.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumberArray, self).__init__()

        self.values = None                                # unicode


class OnlineResource(object):
    """A concrete class within the cim v2 type system.

    An approximation of ISO19115 CI_ONLINERESOURCE.

    """
    def __init__(self):
        """Constructor.

        """
        super(OnlineResource, self).__init__()

        self.description = None                           # unicode
        self.linkage = None                               # unicode
        self.name = None                                  # unicode
        self.protocol = None                              # unicode


class Party(object):
    """A concrete class within the cim v2 type system.

    Implements minimal material for an ISO19115-1 (2014) compliant party. 
    For our purposes this is a much better animal than the previous responsibleParty 
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

    """
    def __init__(self):
        """Constructor.

        """
        super(Party, self).__init__()

        self.address = None                               # unicode
        self.email = None                                 # unicode
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo
        self.name = None                                  # unicode
        self.organisation = None                          # bool
        self.url = None                                   # shared.OnlineResource


class Pid(object):
    """A concrete class within the cim v2 type system.

    A permanent identifier (with a resolution service).

    """
    def __init__(self):
        """Constructor.

        """
        super(Pid, self).__init__()

        self.id = None                                    # unicode
        self.resolution_service = None                    # shared.OnlineResource


class Responsibility(object):
    """A concrete class within the cim v2 type system.

    Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty).

    """
    def __init__(self):
        """Constructor.

        """
        super(Responsibility, self).__init__()

        self.link_to_party = []                           # shared.DocReference
        self.party = []                                   # shared.Party
        self.role = None                                  # shared.RoleCode
        self.when = None                                  # shared.TimePeriod


class StandaloneDocument(object):
    """An abstract class within the cim v2 type system.

    Raw base class for documents which are created standalone in a workflow.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(StandaloneDocument, self).__init__()

        self.long_name = None                             # unicode
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo
        self.name = None                                  # unicode
        self.references = []                              # shared.Citation
        self.responsible_parties = []                     # shared.Responsibility


class TimePeriod(object):
    """A concrete class within the cim v2 type system.

    Creates a time period class aka a temporal extent.

    """
    def __init__(self):
        """Constructor.

        """
        super(TimePeriod, self).__init__()

        self.calendar = None                              # shared.Calendar
        self.date = None                                  # shared.DateTime
        self.date_type = None                             # shared.PeriodDateTypes
        self.length = None                                # int
        self.units = None                                 # shared.TimeUnits


class TimesliceList(object):
    """A concrete class within the cim v2 type system.

    A list of referential dates, 
        e.g. yearlist, 1,4,5 would refer to jan,april,may,
             monthlist, 1,5,6 would refer to the 1st, 5th and 6th of the month.

    """
    def __init__(self):
        """Constructor.

        """
        super(TimesliceList, self).__init__()

        self.members = None                               # shared.NumberArray
        self.units = None                                 # shared.SlicetimeUnits


class VocabMember(object):
    """A concrete class within the cim v2 type system.

    A term in an external (to the CIM) controlled vocabulary (CV).

    """
    def __init__(self):
        """Constructor.

        """
        super(VocabMember, self).__init__()

        self.uri = None                                   # unicode
        self.value = None                                 # unicode
        self.vocab = None                                 # shared.Citation


class CimLink(OnlineResource):
    """A concrete class within the cim v2 type system.

    Specialisation of online resource for link between CIM documents.

    """
    def __init__(self):
        """Constructor.

        """
        super(CimLink, self).__init__()

        self.remote_type = None                           # unicode


class IrregularDateset(DatetimeSet):
    """A concrete class within the cim v2 type system.

    Creates a set of irregularly spaced times.

    """
    def __init__(self):
        """Constructor.

        """
        super(IrregularDateset, self).__init__()

        self.date_set = None                              # unicode


class Reference(Citation):
    """A concrete class within the cim v2 type system.

    A citation which is forced to have a context provided.

    """
    def __init__(self):
        """Constructor.

        """
        super(Reference, self).__init__()



class RegularTimeset(DatetimeSet):
    """A concrete class within the cim v2 type system.

    Creates a regularly spaced set of times.

    """
    def __init__(self):
        """Constructor.

        """
        super(RegularTimeset, self).__init__()

        self.increment = None                             # shared.TimePeriod
        self.length = None                                # int
        self.start_date = None                            # shared.DateTime


class CalendarTypes(object):
    """An enumeration within the cim v2 type system.

    Create and return a calendar type enum.
    """

    pass


class PeriodDateTypes(object):
    """An enumeration within the cim v2 type system.

    Create and return a period date type enum (used by time_period).
    """

    pass


class RoleCode(object):
    """An enumeration within the cim v2 type system.

    Responsibility role codes.
    """

    pass


class SlicetimeUnits(object):
    """An enumeration within the cim v2 type system.

    Create and return a time unit enum for just years and months.
    """

    pass


class TextCode(object):
    """An enumeration within the cim v2 type system.

    Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.
    """

    pass


class TimeUnits(object):
    """An enumeration within the cim v2 type system.

    Create and return a time unit enum.
    """

    pass


