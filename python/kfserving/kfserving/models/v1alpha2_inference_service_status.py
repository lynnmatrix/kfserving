# coding: utf-8

"""
    KFServing

    Python SDK for KFServing  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kfserving.models.knative_addressable import KnativeAddressable  # noqa: F401,E501
from kfserving.models.knative_condition import KnativeCondition  # noqa: F401,E501
from kfserving.models.v1alpha2_status_configuration_spec import V1alpha2StatusConfigurationSpec  # noqa: F401,E501


class V1alpha2InferenceServiceStatus(object):
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
        'address': 'KnativeAddressable',
        'canary': 'dict(str, V1alpha2StatusConfigurationSpec)',
        'canary_traffic': 'int',
        'conditions': 'list[KnativeCondition]',
        'default': 'dict(str, V1alpha2StatusConfigurationSpec)',
        'observed_generation': 'int',
        'traffic': 'int',
        'url': 'str'
    }

    attribute_map = {
        'address': 'address',
        'canary': 'canary',
        'canary_traffic': 'canaryTraffic',
        'conditions': 'conditions',
        'default': 'default',
        'observed_generation': 'observedGeneration',
        'traffic': 'traffic',
        'url': 'url'
    }

    def __init__(self, address=None, canary=None, canary_traffic=None, conditions=None, default=None, observed_generation=None, traffic=None, url=None):  # noqa: E501
        """V1alpha2InferenceServiceStatus - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._canary = None
        self._canary_traffic = None
        self._conditions = None
        self._default = None
        self._observed_generation = None
        self._traffic = None
        self._url = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if canary is not None:
            self.canary = canary
        if canary_traffic is not None:
            self.canary_traffic = canary_traffic
        if conditions is not None:
            self.conditions = conditions
        if default is not None:
            self.default = default
        if observed_generation is not None:
            self.observed_generation = observed_generation
        if traffic is not None:
            self.traffic = traffic
        if url is not None:
            self.url = url

    @property
    def address(self):
        """Gets the address of this V1alpha2InferenceServiceStatus.  # noqa: E501

        Addressable URL for eventing  # noqa: E501

        :return: The address of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :rtype: KnativeAddressable
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this V1alpha2InferenceServiceStatus.

        Addressable URL for eventing  # noqa: E501

        :param address: The address of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :type: KnativeAddressable
        """

        self._address = address

    @property
    def canary(self):
        """Gets the canary of this V1alpha2InferenceServiceStatus.  # noqa: E501

        Statuses for the canary endpoints of the InferenceService  # noqa: E501

        :return: The canary of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :rtype: dict(str, V1alpha2StatusConfigurationSpec)
        """
        return self._canary

    @canary.setter
    def canary(self, canary):
        """Sets the canary of this V1alpha2InferenceServiceStatus.

        Statuses for the canary endpoints of the InferenceService  # noqa: E501

        :param canary: The canary of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :type: dict(str, V1alpha2StatusConfigurationSpec)
        """

        self._canary = canary

    @property
    def canary_traffic(self):
        """Gets the canary_traffic of this V1alpha2InferenceServiceStatus.  # noqa: E501

        Traffic percentage that goes to canary services  # noqa: E501

        :return: The canary_traffic of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :rtype: int
        """
        return self._canary_traffic

    @canary_traffic.setter
    def canary_traffic(self, canary_traffic):
        """Sets the canary_traffic of this V1alpha2InferenceServiceStatus.

        Traffic percentage that goes to canary services  # noqa: E501

        :param canary_traffic: The canary_traffic of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :type: int
        """

        self._canary_traffic = canary_traffic

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha2InferenceServiceStatus.  # noqa: E501

        Conditions the latest available observations of a resource's current state.  # noqa: E501

        :return: The conditions of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :rtype: list[KnativeCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha2InferenceServiceStatus.

        Conditions the latest available observations of a resource's current state.  # noqa: E501

        :param conditions: The conditions of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :type: list[KnativeCondition]
        """

        self._conditions = conditions

    @property
    def default(self):
        """Gets the default of this V1alpha2InferenceServiceStatus.  # noqa: E501

        Statuses for the default endpoints of the InferenceService  # noqa: E501

        :return: The default of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :rtype: dict(str, V1alpha2StatusConfigurationSpec)
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this V1alpha2InferenceServiceStatus.

        Statuses for the default endpoints of the InferenceService  # noqa: E501

        :param default: The default of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :type: dict(str, V1alpha2StatusConfigurationSpec)
        """

        self._default = default

    @property
    def observed_generation(self):
        """Gets the observed_generation of this V1alpha2InferenceServiceStatus.  # noqa: E501

        ObservedGeneration is the 'Generation' of the Service that was last processed by the controller.  # noqa: E501

        :return: The observed_generation of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this V1alpha2InferenceServiceStatus.

        ObservedGeneration is the 'Generation' of the Service that was last processed by the controller.  # noqa: E501

        :param observed_generation: The observed_generation of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def traffic(self):
        """Gets the traffic of this V1alpha2InferenceServiceStatus.  # noqa: E501

        Traffic percentage that goes to default services  # noqa: E501

        :return: The traffic of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :rtype: int
        """
        return self._traffic

    @traffic.setter
    def traffic(self, traffic):
        """Sets the traffic of this V1alpha2InferenceServiceStatus.

        Traffic percentage that goes to default services  # noqa: E501

        :param traffic: The traffic of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :type: int
        """

        self._traffic = traffic

    @property
    def url(self):
        """Gets the url of this V1alpha2InferenceServiceStatus.  # noqa: E501

        URL of the InferenceService  # noqa: E501

        :return: The url of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1alpha2InferenceServiceStatus.

        URL of the InferenceService  # noqa: E501

        :param url: The url of this V1alpha2InferenceServiceStatus.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(V1alpha2InferenceServiceStatus, dict):
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
        if not isinstance(other, V1alpha2InferenceServiceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
