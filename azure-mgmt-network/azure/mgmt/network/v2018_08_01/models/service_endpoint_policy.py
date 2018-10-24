# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class ServiceEndpointPolicy(Resource):
    """Service End point policy resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param service_endpoint_policy_definitions: A collection of service
     endpoint policy definitions of the service endpoint policy.
    :type service_endpoint_policy_definitions:
     list[~azure.mgmt.network.v2018_08_01.models.ServiceEndpointPolicyDefinition]
    :ivar subnets: A collection of references to subnets.
    :vartype subnets: list[~azure.mgmt.network.v2018_08_01.models.Subnet]
    :ivar resource_guid: The resource GUID property of the service endpoint
     policy resource.
    :vartype resource_guid: str
    :ivar provisioning_state: The provisioning state of the service endpoint
     policy. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :vartype provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'subnets': {'readonly': True},
        'resource_guid': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'service_endpoint_policy_definitions': {'key': 'properties.serviceEndpointPolicyDefinitions', 'type': '[ServiceEndpointPolicyDefinition]'},
        'subnets': {'key': 'properties.subnets', 'type': '[Subnet]'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceEndpointPolicy, self).__init__(**kwargs)
        self.service_endpoint_policy_definitions = kwargs.get('service_endpoint_policy_definitions', None)
        self.subnets = None
        self.resource_guid = None
        self.provisioning_state = None
        self.etag = kwargs.get('etag', None)
