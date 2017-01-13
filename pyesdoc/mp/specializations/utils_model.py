# -*- coding: utf-8 -*-

"""
.. module:: model.py
   :platform: Unix, Windows
   :synopsis: A repesentation of CMIP6 specializations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
class TopicSpecialization(object):
    """Wraps a topic specialization.

    """
    def __init__(self):
        """Instance initializer.

        """
        self.authors = None
        self.contact = None
        self.contributors = None
        self.description = None
        self.id = None
        self.qc_status = None
        self.name = None
        self.name_camel_case = None
        self.name_camel_case_spaced = None
        self.parent = None
        self.properties = []
        self.property_sets = []
        self.spec = None
        self.sub_topics = []
        self.type_key = None


    @property
    def all_sub_topics(self):
        """Returns a flattened topic hierarchy.

        """
        def _get(container):
            result = []
            for topic in container.sub_topics:
                result.append(topic)
                result += _get(topic)

            return result

        return _get(self)


    @property
    def all_properties(self):
        """Returns all properties within realm.

        """
        result = []
        for t in self.all_sub_topics:
            result += t.properties
            for ps in t.property_sets:
                result += ps.properties

        return result


    @property
    def all_required_properties(self):
        """Returns all required properties within realm.

        """
        result = []
        for t in self.all_sub_topics:
            result += [i for i in t.properties if i.is_required]
            for ps in t.property_sets:
                result += [i for i in ps.properties if i.is_required]

        return result


    @property
    def all_optional_properties(self):
        """Returns all optional properties within realm.

        """
        result = []
        for t in self.all_sub_topics:
            result += [i for i in t.properties if not i.is_required]
            for ps in t.property_sets:
                result += [i for i in ps.properties if not i.is_required]

        return result


    @property
    def ENUMS(self):
        """Gets associated enumeration definitions.

        """
        try:
            return self.spec.ENUMERATIONS
        except AttributeError:
            try:
                return self.parent.spec.ENUMERATIONS
            except AttributeError:
                return []


    def names(self, offset=None, seperator=" --> ", convertor=None):
        """Returns set of topic names derived from topic specialization id.

        """
        if convertor is None:
            convertor = _to_camel_case_spaced
        names = self.id.split(".")
        if offset is not None:
            names = names[offset:]
        names = [convertor(i) for i in names]
        return seperator.join(names)


class TopicPropertySetSpecialization(object):
    """Wraps a property set specialization.

    """
    def __init__(self):
        """Instance initializer.

        """
        super(TopicPropertySetSpecialization, self).__init__()

        self.description = None
        self.id = None
        self.name = None
        self.name_camel_case = None
        self.name_camel_case_spaced = None
        self.owner = None
        self.properties = []
        self.property_sets = []
        self.topic = None
        self.type_key = "property-set"


    def names(self, offset=None, seperator=" --> ", convertor=None):
        """Returns set of topic names derived from topic specialization id.

        """
        if convertor is None:
            convertor = _to_camel_case_spaced
        names = self.id.split(".")
        if offset is not None:
            names = names[offset:]
        names = [convertor(i) for i in names]
        return seperator.join(names)


class TopicPropertySpecialization(object):
    """Wraps a property specialization.

    """
    def __init__(self):
        """Instance initializer.

        """
        super(TopicPropertySpecialization, self).__init__()

        self.cardinality = None
        self.description = None
        self.enum = None
        self.id = None
        self.name = None
        self.name_camel_case = None
        self.name_camel_case_spaced = None
        self.owner = None
        self.topic = None
        self.typeof = None
        self.type_key = "property"


    @property
    def is_required(self):
        """Gets flag indicating whether cardinality is mandatory or not.

        """
        return self.cardinality.split(".")[0] != "0"


    @property
    def is_collection(self):
        """Gets flag indicating whether property is a collection or not.

        """
        try:
            int(self.cardinality.split(".")[1])
        except ValueError:
            return True
        return False


    @property
    def typeof_label(self):
        """Gets label for the property type.

        """
        if self.typeof == 'str':
            return "STRING"
        elif self.typeof == 'bool':
            return "BOOLEAN"
        elif self.typeof == 'int':
            return "INTEGER"
        elif self.typeof == 'float':
            return "FLOAT"
        elif self.enum:
            return "ENUM"
        return self.typeof.split(":")[-1].upper()


    def validate_value(self, val):
        """Validates a property value.

        :param object val: Value to be validated.

        """
        if self.enum:
            self.enum.validate_value(val)

        if self.typeof == 'str':
            if not isinstance(val, basestring) or not len(val.strip()):
                raise ValueError("Invalid value: must be a non zero length string")

        if self.typeof == 'bool':
            if not isinstance(val, bool):
                raise ValueError("Invalid value: must be a boolean")

        if self.typeof == 'int':
            if not isinstance(val, int):
                raise ValueError("Invalid value: must be an integer")

        if self.typeof == 'float':
            if not isinstance(val, float):
                raise ValueError("Invalid value: must be a float")


class EnumSpecialization(object):
    """Wraps an enumeration specialization.

    """
    def __init__(self):
        """Instance initializer.

        """
        self.choices = []
        self.description = None
        self.id = None
        self.is_open = False
        self.label = None
        self.name = None
        self.type_key = "enum"


    def is_a_member(self, val):
        """Returns flag indicating whether vlue is a member of the enumeration.

        :param object val: Value to be validated.

        """
        return val in [i.value for i in self.choices]


    def validate_value(self, val):
        """Validates a value against the set of enum choices.

        :param object val: Value to be validated.

        """
        if not isinstance(val, basestring) or not len(val.strip()):
            raise ValueError("Invalid value: must be a non zero length string")
        if self.is_a_member(val):
            return
        if not self.is_open:
            raise ValueError("Invalid value: is not an enumeration member")
        if not val.startswith("Other: "):
            raise ValueError("Invalid value: new enumeration members must be prefixed with: 'Other: '")
        other = val.split("Other: ")[-1]
        if self.is_a_member(other):
            raise ValueError("Invalid value: enumeration member already defined")


class EnumChoiceSpecialization(object):
    """Wraps an enumeration choice specialization.

    """
    def __init__(self):
        """Instance initializer.

        """
        self.description = None
        self.enum = None
        self.id = None
        self.value = None
        self.is_other = None
        self.type_key = "enum-choice"


class RealmSpecialization(TopicSpecialization):
    """Wraps a realm specialization.

    """
    def __init__(self):
        """Instance initializer.

        """
        super(RealmSpecialization, self).__init__()
        self.grid = None
        self.key_properties = None
        self.processes = None


def _to_camel_case_spaced(name, separator='_'):
    """Converts passed name to camel case with space.

    :param str name: A name as specified in ontology specification.
    :param str separator: Separator to use in order to split name into constituent parts.

    """
    s = _to_camel_case(name, separator)
    r = s[0]
    for s in s[1:]:
        if s.upper() == s:
            r += " "
        r += s

    return r


def _to_camel_case(name, separator='_'):
    """Converts passed name to camel case.

    :param str name: A name as specified in ontology specification.
    :param str separator: Separator to use in order to split name into constituent parts.

    """
    r = ''
    if name is not None:
        s = name.split(separator)
        for s in s:
            if (len(s) > 0):
                r += s[0].upper()
                if (len(s) > 1):
                    r += s[1:]
    return r