# coding: utf-8

"""
    蓝鲸用户管理 API

    蓝鲸用户管理后台服务 API  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class DynamicFields(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'options': 'object',
        'default': 'object',
        'display_name': 'str',
        'display_name_en': 'str',
        'display_name_zh_hans': 'str',
        'type': 'str',
        'require': 'bool',
        'unique': 'bool',
        'editable': 'bool',
        'configurable': 'bool',
        'builtin': 'bool',
        'order': 'int',
        'enabled': 'bool',
        'visible': 'bool',
        'map_method': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'options': 'options',
        'default': 'default',
        'display_name': 'display_name',
        'display_name_en': 'display_name_en',
        'display_name_zh_hans': 'display_name_zh_hans',
        'type': 'type',
        'require': 'require',
        'unique': 'unique',
        'editable': 'editable',
        'configurable': 'configurable',
        'builtin': 'builtin',
        'order': 'order',
        'enabled': 'enabled',
        'visible': 'visible',
        'map_method': 'map_method'
    }

    def __init__(self, id=None, name=None, options=None, default=None, display_name=None, display_name_en=None, display_name_zh_hans=None, type=None, require=None, unique=None, editable=None, configurable=None, builtin=None, order=None, enabled=None, visible=None, map_method=None):  # noqa: E501
        """DynamicFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._options = None
        self._default = None
        self._display_name = None
        self._display_name_en = None
        self._display_name_zh_hans = None
        self._type = None
        self._require = None
        self._unique = None
        self._editable = None
        self._configurable = None
        self._builtin = None
        self._order = None
        self._enabled = None
        self._visible = None
        self._map_method = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if options is not None:
            self.options = options
        if default is not None:
            self.default = default
        self.display_name = display_name
        if display_name_en is not None:
            self.display_name_en = display_name_en
        if display_name_zh_hans is not None:
            self.display_name_zh_hans = display_name_zh_hans
        self.type = type
        if require is not None:
            self.require = require
        if unique is not None:
            self.unique = unique
        if editable is not None:
            self.editable = editable
        if configurable is not None:
            self.configurable = configurable
        if builtin is not None:
            self.builtin = builtin
        self.order = order
        if enabled is not None:
            self.enabled = enabled
        if visible is not None:
            self.visible = visible
        if map_method is not None:
            self.map_method = map_method

    @property
    def id(self):
        """Gets the id of this DynamicFields.  # noqa: E501


        :return: The id of this DynamicFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DynamicFields.


        :param id: The id of this DynamicFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DynamicFields.  # noqa: E501


        :return: The name of this DynamicFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DynamicFields.


        :param name: The name of this DynamicFields.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def options(self):
        """Gets the options of this DynamicFields.  # noqa: E501


        :return: The options of this DynamicFields.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DynamicFields.


        :param options: The options of this DynamicFields.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def default(self):
        """Gets the default of this DynamicFields.  # noqa: E501


        :return: The default of this DynamicFields.  # noqa: E501
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this DynamicFields.


        :param default: The default of this DynamicFields.  # noqa: E501
        :type: object
        """

        self._default = default

    @property
    def display_name(self):
        """Gets the display_name of this DynamicFields.  # noqa: E501


        :return: The display_name of this DynamicFields.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DynamicFields.


        :param display_name: The display_name of this DynamicFields.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def display_name_en(self):
        """Gets the display_name_en of this DynamicFields.  # noqa: E501


        :return: The display_name_en of this DynamicFields.  # noqa: E501
        :rtype: str
        """
        return self._display_name_en

    @display_name_en.setter
    def display_name_en(self, display_name_en):
        """Sets the display_name_en of this DynamicFields.


        :param display_name_en: The display_name_en of this DynamicFields.  # noqa: E501
        :type: str
        """

        self._display_name_en = display_name_en

    @property
    def display_name_zh_hans(self):
        """Gets the display_name_zh_hans of this DynamicFields.  # noqa: E501


        :return: The display_name_zh_hans of this DynamicFields.  # noqa: E501
        :rtype: str
        """
        return self._display_name_zh_hans

    @display_name_zh_hans.setter
    def display_name_zh_hans(self, display_name_zh_hans):
        """Sets the display_name_zh_hans of this DynamicFields.


        :param display_name_zh_hans: The display_name_zh_hans of this DynamicFields.  # noqa: E501
        :type: str
        """

        self._display_name_zh_hans = display_name_zh_hans

    @property
    def type(self):
        """Gets the type of this DynamicFields.  # noqa: E501


        :return: The type of this DynamicFields.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DynamicFields.


        :param type: The type of this DynamicFields.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["string", "one_enum", "multi_enum", "number", "timer"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def require(self):
        """Gets the require of this DynamicFields.  # noqa: E501


        :return: The require of this DynamicFields.  # noqa: E501
        :rtype: bool
        """
        return self._require

    @require.setter
    def require(self, require):
        """Sets the require of this DynamicFields.


        :param require: The require of this DynamicFields.  # noqa: E501
        :type: bool
        """

        self._require = require

    @property
    def unique(self):
        """Gets the unique of this DynamicFields.  # noqa: E501


        :return: The unique of this DynamicFields.  # noqa: E501
        :rtype: bool
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this DynamicFields.


        :param unique: The unique of this DynamicFields.  # noqa: E501
        :type: bool
        """

        self._unique = unique

    @property
    def editable(self):
        """Gets the editable of this DynamicFields.  # noqa: E501


        :return: The editable of this DynamicFields.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this DynamicFields.


        :param editable: The editable of this DynamicFields.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def configurable(self):
        """Gets the configurable of this DynamicFields.  # noqa: E501


        :return: The configurable of this DynamicFields.  # noqa: E501
        :rtype: bool
        """
        return self._configurable

    @configurable.setter
    def configurable(self, configurable):
        """Sets the configurable of this DynamicFields.


        :param configurable: The configurable of this DynamicFields.  # noqa: E501
        :type: bool
        """

        self._configurable = configurable

    @property
    def builtin(self):
        """Gets the builtin of this DynamicFields.  # noqa: E501


        :return: The builtin of this DynamicFields.  # noqa: E501
        :rtype: bool
        """
        return self._builtin

    @builtin.setter
    def builtin(self, builtin):
        """Sets the builtin of this DynamicFields.


        :param builtin: The builtin of this DynamicFields.  # noqa: E501
        :type: bool
        """

        self._builtin = builtin

    @property
    def order(self):
        """Gets the order of this DynamicFields.  # noqa: E501


        :return: The order of this DynamicFields.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this DynamicFields.


        :param order: The order of this DynamicFields.  # noqa: E501
        :type: int
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

    @property
    def enabled(self):
        """Gets the enabled of this DynamicFields.  # noqa: E501


        :return: The enabled of this DynamicFields.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DynamicFields.


        :param enabled: The enabled of this DynamicFields.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def visible(self):
        """Gets the visible of this DynamicFields.  # noqa: E501


        :return: The visible of this DynamicFields.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this DynamicFields.


        :param visible: The visible of this DynamicFields.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def map_method(self):
        """Gets the map_method of this DynamicFields.  # noqa: E501


        :return: The map_method of this DynamicFields.  # noqa: E501
        :rtype: str
        """
        return self._map_method

    @map_method.setter
    def map_method(self, map_method):
        """Sets the map_method of this DynamicFields.


        :param map_method: The map_method of this DynamicFields.  # noqa: E501
        :type: str
        """
        allowed_values = ["direct", "custom"]  # noqa: E501
        if map_method not in allowed_values:
            raise ValueError(
                "Invalid value for `map_method` ({0}), must be one of {1}"  # noqa: E501
                .format(map_method, allowed_values)
            )

        self._map_method = map_method

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DynamicFields, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DynamicFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
