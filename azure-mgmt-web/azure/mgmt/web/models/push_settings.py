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


class PushSettings(Model):
    """Push settings for the App.

    :param is_push_enabled: Gets or sets a flag indicating whether the Push
     endpoint is enabled.
    :type is_push_enabled: bool
    :param tag_whitelist_json: Gets or sets a JSON string containing a list of
     tags that are whitelisted for use by the push registration endpoint.
    :type tag_whitelist_json: str
    :param tags_requiring_auth: Gets or sets a JSON string containing a list
     of tags that require user authentication to be used in the push
     registration endpoint.
     Tags can consist of alphanumeric characters and the following:
     '_', '@', '#', '.', ':', '-'.
     Validation should be performed at the PushRequestHandler.
    :type tags_requiring_auth: str
    :param dynamic_tags_json: Gets or sets a JSON string containing a list of
     dynamic tags that will be evaluated from user claims in the push
     registration endpoint.
    :type dynamic_tags_json: str
    """

    _validation = {
        'is_push_enabled': {'required': True},
    }

    _attribute_map = {
        'is_push_enabled': {'key': 'isPushEnabled', 'type': 'bool'},
        'tag_whitelist_json': {'key': 'tagWhitelistJson', 'type': 'str'},
        'tags_requiring_auth': {'key': 'tagsRequiringAuth', 'type': 'str'},
        'dynamic_tags_json': {'key': 'dynamicTagsJson', 'type': 'str'},
    }

    def __init__(self, is_push_enabled, tag_whitelist_json=None, tags_requiring_auth=None, dynamic_tags_json=None):
        self.is_push_enabled = is_push_enabled
        self.tag_whitelist_json = tag_whitelist_json
        self.tags_requiring_auth = tags_requiring_auth
        self.dynamic_tags_json = dynamic_tags_json