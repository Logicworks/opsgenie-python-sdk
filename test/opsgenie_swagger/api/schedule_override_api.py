# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from opsgenie_swagger.api_client import ApiClient


class ScheduleOverrideApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_schedule_override(self, identifier, body, **kwargs):  # noqa: E501
        """Create Schedule Override  # noqa: E501

        Creates a schedule override for the specified user and schedule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_schedule_override(identifier, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param CreateScheduleOverridePayload body: Request payload of created schedule override (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: CreateScheduleOverrideResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_schedule_override_with_http_info(identifier, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_schedule_override_with_http_info(identifier, body, **kwargs)  # noqa: E501
            return data

    def create_schedule_override_with_http_info(self, identifier, body, **kwargs):  # noqa: E501
        """Create Schedule Override  # noqa: E501

        Creates a schedule override for the specified user and schedule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_schedule_override_with_http_info(identifier, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param CreateScheduleOverridePayload body: Request payload of created schedule override (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: CreateScheduleOverrideResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'body', 'schedule_identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_schedule_override" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `create_schedule_override`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_schedule_override`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'schedule_identifier_type' in params:
            query_params.append(('scheduleIdentifierType', params['schedule_identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/schedules/{identifier}/overrides', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateScheduleOverrideResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_schedule_override(self, identifier, alias, **kwargs):  # noqa: E501
        """Delete Schedule Override  # noqa: E501

        Delete schedule override with given alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_schedule_override(identifier, alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str alias: Alias of the schedule override (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_schedule_override_with_http_info(identifier, alias, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_schedule_override_with_http_info(identifier, alias, **kwargs)  # noqa: E501
            return data

    def delete_schedule_override_with_http_info(self, identifier, alias, **kwargs):  # noqa: E501
        """Delete Schedule Override  # noqa: E501

        Delete schedule override with given alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_schedule_override_with_http_info(identifier, alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str alias: Alias of the schedule override (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'alias', 'schedule_identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_schedule_override" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `delete_schedule_override`")  # noqa: E501
        # verify the required parameter 'alias' is set
        if ('alias' not in params or
                params['alias'] is None):
            raise ValueError("Missing the required parameter `alias` when calling `delete_schedule_override`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'alias' in params:
            path_params['alias'] = params['alias']  # noqa: E501

        query_params = []
        if 'schedule_identifier_type' in params:
            query_params.append(('scheduleIdentifierType', params['schedule_identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/schedules/{identifier}/overrides/{alias}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_schedule_override(self, identifier, alias, **kwargs):  # noqa: E501
        """Get Schedule Override  # noqa: E501

        Gets schedule override details with given alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schedule_override(identifier, alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str alias: Alias of the schedule override (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: GetScheduleOverrideResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_schedule_override_with_http_info(identifier, alias, **kwargs)  # noqa: E501
        else:
            (data) = self.get_schedule_override_with_http_info(identifier, alias, **kwargs)  # noqa: E501
            return data

    def get_schedule_override_with_http_info(self, identifier, alias, **kwargs):  # noqa: E501
        """Get Schedule Override  # noqa: E501

        Gets schedule override details with given alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schedule_override_with_http_info(identifier, alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str alias: Alias of the schedule override (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: GetScheduleOverrideResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'alias', 'schedule_identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_schedule_override" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_schedule_override`")  # noqa: E501
        # verify the required parameter 'alias' is set
        if ('alias' not in params or
                params['alias'] is None):
            raise ValueError("Missing the required parameter `alias` when calling `get_schedule_override`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'alias' in params:
            path_params['alias'] = params['alias']  # noqa: E501

        query_params = []
        if 'schedule_identifier_type' in params:
            query_params.append(('scheduleIdentifierType', params['schedule_identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/schedules/{identifier}/overrides/{alias}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetScheduleOverrideResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_schedule_override(self, identifier, **kwargs):  # noqa: E501
        """List Schedule Overrides  # noqa: E501

        Returns list of schedule overrides  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_schedule_override(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: ListScheduleOverrideResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_schedule_override_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.list_schedule_override_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def list_schedule_override_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """List Schedule Overrides  # noqa: E501

        Returns list of schedule overrides  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_schedule_override_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: ListScheduleOverrideResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'schedule_identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_schedule_override" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `list_schedule_override`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'schedule_identifier_type' in params:
            query_params.append(('scheduleIdentifierType', params['schedule_identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/schedules/{identifier}/overrides', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListScheduleOverrideResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_schedule_override(self, identifier, alias, body, **kwargs):  # noqa: E501
        """Update Schedule Override  # noqa: E501

        Update schedule override with given alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schedule_override(identifier, alias, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str alias: Alias of the schedule override (required)
        :param UpdateScheduleOverridePayload body: Request payload of update schedule override (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: UpdateScheduleOverrideResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_schedule_override_with_http_info(identifier, alias, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_schedule_override_with_http_info(identifier, alias, body, **kwargs)  # noqa: E501
            return data

    def update_schedule_override_with_http_info(self, identifier, alias, body, **kwargs):  # noqa: E501
        """Update Schedule Override  # noqa: E501

        Update schedule override with given alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schedule_override_with_http_info(identifier, alias, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str alias: Alias of the schedule override (required)
        :param UpdateScheduleOverridePayload body: Request payload of update schedule override (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: UpdateScheduleOverrideResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'alias', 'body', 'schedule_identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_schedule_override" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_schedule_override`")  # noqa: E501
        # verify the required parameter 'alias' is set
        if ('alias' not in params or
                params['alias'] is None):
            raise ValueError("Missing the required parameter `alias` when calling `update_schedule_override`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_schedule_override`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'alias' in params:
            path_params['alias'] = params['alias']  # noqa: E501

        query_params = []
        if 'schedule_identifier_type' in params:
            query_params.append(('scheduleIdentifierType', params['schedule_identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/schedules/{identifier}/overrides/{alias}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateScheduleOverrideResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
