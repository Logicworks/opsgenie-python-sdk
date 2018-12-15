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


class ScheduleRotationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_schedule_rotation(self, identifier, body, **kwargs):  # noqa: E501
        """Create Schedule Rotation  # noqa: E501

        Creates a new schedule rotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_schedule_rotation(identifier, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param CreateScheduleRotationPayload body: Request payload of created schedule rotation (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_schedule_rotation_with_http_info(identifier, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_schedule_rotation_with_http_info(identifier, body, **kwargs)  # noqa: E501
            return data

    def create_schedule_rotation_with_http_info(self, identifier, body, **kwargs):  # noqa: E501
        """Create Schedule Rotation  # noqa: E501

        Creates a new schedule rotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_schedule_rotation_with_http_info(identifier, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param CreateScheduleRotationPayload body: Request payload of created schedule rotation (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
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
                    " to method create_schedule_rotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `create_schedule_rotation`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_schedule_rotation`")  # noqa: E501

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
            '/v2/schedules/{identifier}/rotations', 'POST',
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

    def delete_schedule_rotation(self, identifier, id, **kwargs):  # noqa: E501
        """Delete Schedule Rotation  # noqa: E501

        Delete schedule rotation with given identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_schedule_rotation(identifier, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str id: Identifier of schedule rotation (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_schedule_rotation_with_http_info(identifier, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_schedule_rotation_with_http_info(identifier, id, **kwargs)  # noqa: E501
            return data

    def delete_schedule_rotation_with_http_info(self, identifier, id, **kwargs):  # noqa: E501
        """Delete Schedule Rotation  # noqa: E501

        Delete schedule rotation with given identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_schedule_rotation_with_http_info(identifier, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str id: Identifier of schedule rotation (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'id', 'schedule_identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_schedule_rotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `delete_schedule_rotation`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_schedule_rotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v2/schedules/{identifier}/rotations/{id}', 'DELETE',
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

    def get_schedule_rotation(self, identifier, id, **kwargs):  # noqa: E501
        """Get Schedule Rotation  # noqa: E501

        Returns schedule rotation with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schedule_rotation(identifier, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str id: Identifier of schedule rotation (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: GetScheduleRotationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_schedule_rotation_with_http_info(identifier, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_schedule_rotation_with_http_info(identifier, id, **kwargs)  # noqa: E501
            return data

    def get_schedule_rotation_with_http_info(self, identifier, id, **kwargs):  # noqa: E501
        """Get Schedule Rotation  # noqa: E501

        Returns schedule rotation with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schedule_rotation_with_http_info(identifier, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str id: Identifier of schedule rotation (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: GetScheduleRotationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'id', 'schedule_identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_schedule_rotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_schedule_rotation`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_schedule_rotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v2/schedules/{identifier}/rotations/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetScheduleRotationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_schedule_rotations(self, identifier, **kwargs):  # noqa: E501
        """List Schedule Rotations  # noqa: E501

        Returns list of schedule rotations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_schedule_rotations(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: ListScheduleRotationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_schedule_rotations_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.list_schedule_rotations_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def list_schedule_rotations_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """List Schedule Rotations  # noqa: E501

        Returns list of schedule rotations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_schedule_rotations_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: ListScheduleRotationsResponse
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
                    " to method list_schedule_rotations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `list_schedule_rotations`")  # noqa: E501

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
            '/v2/schedules/{identifier}/rotations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListScheduleRotationsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_schedule_rotation(self, identifier, id, body, **kwargs):  # noqa: E501
        """Update Schedule Rotation (Partial)  # noqa: E501

        Update schedule rotation with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schedule_rotation(identifier, id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str id: Identifier of schedule rotation (required)
        :param UpdateScheduleRotationPayload body: Request payload of update schedule rotation action (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_schedule_rotation_with_http_info(identifier, id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_schedule_rotation_with_http_info(identifier, id, body, **kwargs)  # noqa: E501
            return data

    def update_schedule_rotation_with_http_info(self, identifier, id, body, **kwargs):  # noqa: E501
        """Update Schedule Rotation (Partial)  # noqa: E501

        Update schedule rotation with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schedule_rotation_with_http_info(identifier, id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of schedule which could be id or name (required)
        :param str id: Identifier of schedule rotation (required)
        :param UpdateScheduleRotationPayload body: Request payload of update schedule rotation action (required)
        :param str schedule_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'id', 'body', 'schedule_identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_schedule_rotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_schedule_rotation`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_schedule_rotation`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_schedule_rotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v2/schedules/{identifier}/rotations/{id}', 'PATCH',
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