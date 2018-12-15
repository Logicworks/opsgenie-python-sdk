# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateHeartbeatPayload(object):
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
        'name': 'str',
        'description': 'str',
        'interval': 'int',
        'interval_unit': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'interval': 'interval',
        'interval_unit': 'intervalUnit',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, description=None, interval=None, interval_unit=None, enabled=None):  # noqa: E501
        """CreateHeartbeatPayload - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._interval = None
        self._interval_unit = None
        self._enabled = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.interval = interval
        self.interval_unit = interval_unit
        self.enabled = enabled

    @property
    def name(self):
        """Gets the name of this CreateHeartbeatPayload.  # noqa: E501

        Name of the heartbeat  # noqa: E501

        :return: The name of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateHeartbeatPayload.

        Name of the heartbeat  # noqa: E501

        :param name: The name of this CreateHeartbeatPayload.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateHeartbeatPayload.  # noqa: E501

        An optional description of the heartbeat  # noqa: E501

        :return: The description of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateHeartbeatPayload.

        An optional description of the heartbeat  # noqa: E501

        :param description: The description of this CreateHeartbeatPayload.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 10000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `10000`")  # noqa: E501

        self._description = description

    @property
    def interval(self):
        """Gets the interval of this CreateHeartbeatPayload.  # noqa: E501

        Specifies how often a heartbeat message should be expected  # noqa: E501

        :return: The interval of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this CreateHeartbeatPayload.

        Specifies how often a heartbeat message should be expected  # noqa: E501

        :param interval: The interval of this CreateHeartbeatPayload.  # noqa: E501
        :type: int
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501
        if interval is not None and interval < 1:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value greater than or equal to `1`")  # noqa: E501

        self._interval = interval

    @property
    def interval_unit(self):
        """Gets the interval_unit of this CreateHeartbeatPayload.  # noqa: E501

        Interval specified as 'minutes', 'hours' or 'days'  # noqa: E501

        :return: The interval_unit of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: str
        """
        return self._interval_unit

    @interval_unit.setter
    def interval_unit(self, interval_unit):
        """Sets the interval_unit of this CreateHeartbeatPayload.

        Interval specified as 'minutes', 'hours' or 'days'  # noqa: E501

        :param interval_unit: The interval_unit of this CreateHeartbeatPayload.  # noqa: E501
        :type: str
        """
        if interval_unit is None:
            raise ValueError("Invalid value for `interval_unit`, must not be `None`")  # noqa: E501
        allowed_values = ["minutes", "hours", "days"]  # noqa: E501
        if interval_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `interval_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(interval_unit, allowed_values)
            )

        self._interval_unit = interval_unit

    @property
    def enabled(self):
        """Gets the enabled of this CreateHeartbeatPayload.  # noqa: E501

        Enable/disable heartbeat monitoring  # noqa: E501

        :return: The enabled of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateHeartbeatPayload.

        Enable/disable heartbeat monitoring  # noqa: E501

        :param enabled: The enabled of this CreateHeartbeatPayload.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateHeartbeatPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other