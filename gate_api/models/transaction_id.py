# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class TransactionID(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {'tx_id': 'int'}

    attribute_map = {'tx_id': 'tx_id'}

    def __init__(self, tx_id=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, Configuration) -> None
        """TransactionID - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tx_id = None
        self.discriminator = None

        if tx_id is not None:
            self.tx_id = tx_id

    @property
    def tx_id(self):
        """Gets the tx_id of this TransactionID.  # noqa: E501

        Order id  # noqa: E501

        :return: The tx_id of this TransactionID.  # noqa: E501
        :rtype: int
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this TransactionID.

        Order id  # noqa: E501

        :param tx_id: The tx_id of this TransactionID.  # noqa: E501
        :type: int
        """

        self._tx_id = tx_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, TransactionID):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionID):
            return True

        return self.to_dict() != other.to_dict()