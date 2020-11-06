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

from kfserving.models.v1alpha2_explainer_spec import V1alpha2ExplainerSpec  # noqa: F401,E501
from kfserving.models.v1alpha2_predictor_spec import V1alpha2PredictorSpec  # noqa: F401,E501
from kfserving.models.v1alpha2_transformer_spec import V1alpha2TransformerSpec  # noqa: F401,E501


class V1alpha2EndpointSpec(object):
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
        'explainer': 'V1alpha2ExplainerSpec',
        'predictor': 'V1alpha2PredictorSpec',
        'transformer': 'V1alpha2TransformerSpec'
    }

    attribute_map = {
        'explainer': 'explainer',
        'predictor': 'predictor',
        'transformer': 'transformer'
    }

    def __init__(self, explainer=None, predictor=None, transformer=None):  # noqa: E501
        """V1alpha2EndpointSpec - a model defined in Swagger"""  # noqa: E501

        self._explainer = None
        self._predictor = None
        self._transformer = None
        self.discriminator = None

        if explainer is not None:
            self.explainer = explainer
        self.predictor = predictor
        if transformer is not None:
            self.transformer = transformer

    @property
    def explainer(self):
        """Gets the explainer of this V1alpha2EndpointSpec.  # noqa: E501

        Explainer defines the model explanation service spec, explainer service calls to predictor or transformer if it is specified.  # noqa: E501

        :return: The explainer of this V1alpha2EndpointSpec.  # noqa: E501
        :rtype: V1alpha2ExplainerSpec
        """
        return self._explainer

    @explainer.setter
    def explainer(self, explainer):
        """Sets the explainer of this V1alpha2EndpointSpec.

        Explainer defines the model explanation service spec, explainer service calls to predictor or transformer if it is specified.  # noqa: E501

        :param explainer: The explainer of this V1alpha2EndpointSpec.  # noqa: E501
        :type: V1alpha2ExplainerSpec
        """

        self._explainer = explainer

    @property
    def predictor(self):
        """Gets the predictor of this V1alpha2EndpointSpec.  # noqa: E501

        Predictor defines the model serving spec  # noqa: E501

        :return: The predictor of this V1alpha2EndpointSpec.  # noqa: E501
        :rtype: V1alpha2PredictorSpec
        """
        return self._predictor

    @predictor.setter
    def predictor(self, predictor):
        """Sets the predictor of this V1alpha2EndpointSpec.

        Predictor defines the model serving spec  # noqa: E501

        :param predictor: The predictor of this V1alpha2EndpointSpec.  # noqa: E501
        :type: V1alpha2PredictorSpec
        """
        if predictor is None:
            raise ValueError("Invalid value for `predictor`, must not be `None`")  # noqa: E501

        self._predictor = predictor

    @property
    def transformer(self):
        """Gets the transformer of this V1alpha2EndpointSpec.  # noqa: E501

        Transformer defines the pre/post processing before and after the predictor call, transformer service calls to predictor service.  # noqa: E501

        :return: The transformer of this V1alpha2EndpointSpec.  # noqa: E501
        :rtype: V1alpha2TransformerSpec
        """
        return self._transformer

    @transformer.setter
    def transformer(self, transformer):
        """Sets the transformer of this V1alpha2EndpointSpec.

        Transformer defines the pre/post processing before and after the predictor call, transformer service calls to predictor service.  # noqa: E501

        :param transformer: The transformer of this V1alpha2EndpointSpec.  # noqa: E501
        :type: V1alpha2TransformerSpec
        """

        self._transformer = transformer

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
        if issubclass(V1alpha2EndpointSpec, dict):
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
        if not isinstance(other, V1alpha2EndpointSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
