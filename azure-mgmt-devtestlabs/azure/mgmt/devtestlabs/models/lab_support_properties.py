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

from msrest.serialization import Model


class LabSupportProperties(Model):
    """Properties of a lab's support banner.

    :param enabled: Is the lab support banner active/enabled at this time?.
     Possible values include: 'Enabled', 'Disabled'
    :type enabled: str or ~azure.mgmt.devtestlabs.models.EnableStatus
    :param markdown: The markdown text (if any) that this lab displays in the
     UI. If left empty/null, nothing will be shown.
    :type markdown: str
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'str'},
        'markdown': {'key': 'markdown', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LabSupportProperties, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.markdown = kwargs.get('markdown', None)
