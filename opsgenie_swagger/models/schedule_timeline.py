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

from opsgenie_swagger.models.schedule_meta import ScheduleMeta  # noqa: F401,E501
from opsgenie_swagger.models.timeline import Timeline  # noqa: F401,E501


class ScheduleTimeline(object):
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
        'parent': 'ScheduleMeta',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'final_timeline': 'Timeline',
        'base_timeline': 'Timeline',
        'override_timeline': 'Timeline',
        'forwarding_timeline': 'Timeline'
    }

    attribute_map = {
        'parent': '_parent',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'final_timeline': 'finalTimeline',
        'base_timeline': 'baseTimeline',
        'override_timeline': 'overrideTimeline',
        'forwarding_timeline': 'forwardingTimeline'
    }

    def __init__(self, parent=None, start_date=None, end_date=None, final_timeline=None, base_timeline=None, override_timeline=None, forwarding_timeline=None):  # noqa: E501
        """ScheduleTimeline - a model defined in Swagger"""  # noqa: E501

        self._parent = None
        self._start_date = None
        self._end_date = None
        self._final_timeline = None
        self._base_timeline = None
        self._override_timeline = None
        self._forwarding_timeline = None
        self.discriminator = None

        if parent is not None:
            self.parent = parent
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if final_timeline is not None:
            self.final_timeline = final_timeline
        if base_timeline is not None:
            self.base_timeline = base_timeline
        if override_timeline is not None:
            self.override_timeline = override_timeline
        if forwarding_timeline is not None:
            self.forwarding_timeline = forwarding_timeline

    @property
    def parent(self):
        """Gets the parent of this ScheduleTimeline.  # noqa: E501


        :return: The parent of this ScheduleTimeline.  # noqa: E501
        :rtype: ScheduleMeta
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ScheduleTimeline.


        :param parent: The parent of this ScheduleTimeline.  # noqa: E501
        :type: ScheduleMeta
        """

        self._parent = parent

    @property
    def start_date(self):
        """Gets the start_date of this ScheduleTimeline.  # noqa: E501


        :return: The start_date of this ScheduleTimeline.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ScheduleTimeline.


        :param start_date: The start_date of this ScheduleTimeline.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ScheduleTimeline.  # noqa: E501


        :return: The end_date of this ScheduleTimeline.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ScheduleTimeline.


        :param end_date: The end_date of this ScheduleTimeline.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def final_timeline(self):
        """Gets the final_timeline of this ScheduleTimeline.  # noqa: E501


        :return: The final_timeline of this ScheduleTimeline.  # noqa: E501
        :rtype: Timeline
        """
        return self._final_timeline

    @final_timeline.setter
    def final_timeline(self, final_timeline):
        """Sets the final_timeline of this ScheduleTimeline.


        :param final_timeline: The final_timeline of this ScheduleTimeline.  # noqa: E501
        :type: Timeline
        """

        self._final_timeline = final_timeline

    @property
    def base_timeline(self):
        """Gets the base_timeline of this ScheduleTimeline.  # noqa: E501


        :return: The base_timeline of this ScheduleTimeline.  # noqa: E501
        :rtype: Timeline
        """
        return self._base_timeline

    @base_timeline.setter
    def base_timeline(self, base_timeline):
        """Sets the base_timeline of this ScheduleTimeline.


        :param base_timeline: The base_timeline of this ScheduleTimeline.  # noqa: E501
        :type: Timeline
        """

        self._base_timeline = base_timeline

    @property
    def override_timeline(self):
        """Gets the override_timeline of this ScheduleTimeline.  # noqa: E501


        :return: The override_timeline of this ScheduleTimeline.  # noqa: E501
        :rtype: Timeline
        """
        return self._override_timeline

    @override_timeline.setter
    def override_timeline(self, override_timeline):
        """Sets the override_timeline of this ScheduleTimeline.


        :param override_timeline: The override_timeline of this ScheduleTimeline.  # noqa: E501
        :type: Timeline
        """

        self._override_timeline = override_timeline

    @property
    def forwarding_timeline(self):
        """Gets the forwarding_timeline of this ScheduleTimeline.  # noqa: E501


        :return: The forwarding_timeline of this ScheduleTimeline.  # noqa: E501
        :rtype: Timeline
        """
        return self._forwarding_timeline

    @forwarding_timeline.setter
    def forwarding_timeline(self, forwarding_timeline):
        """Sets the forwarding_timeline of this ScheduleTimeline.


        :param forwarding_timeline: The forwarding_timeline of this ScheduleTimeline.  # noqa: E501
        :type: Timeline
        """

        self._forwarding_timeline = forwarding_timeline

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
        if not isinstance(other, ScheduleTimeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
