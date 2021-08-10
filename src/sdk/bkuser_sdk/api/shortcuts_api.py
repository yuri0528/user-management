# coding: utf-8

"""
    蓝鲸用户管理 API

    蓝鲸用户管理后台服务 API  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bkuser_sdk.api_client import ApiClient


class ShortcutsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v2_shortcuts_departments_list_tops(self, **kwargs):  # noqa: E501
        """v2_shortcuts_departments_list_tops  # noqa: E501

        获取最顶层的组织列表[权限中心亲和]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_shortcuts_departments_list_tops(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lookup_field: A search term.
        :param str ordering: Which field to use when ordering the results.
        :param int page: A page number within the paginated result set.
        :param int page_size: Number of results to return per page.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_shortcuts_departments_list_tops_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_shortcuts_departments_list_tops_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_shortcuts_departments_list_tops_with_http_info(self, **kwargs):  # noqa: E501
        """v2_shortcuts_departments_list_tops  # noqa: E501

        获取最顶层的组织列表[权限中心亲和]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_shortcuts_departments_list_tops_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lookup_field: A search term.
        :param str ordering: Which field to use when ordering the results.
        :param int page: A page number within the paginated result set.
        :param int page_size: Number of results to return per page.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lookup_field', 'ordering', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_shortcuts_departments_list_tops" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'lookup_field' in params:
            query_params.append(('lookup_field', params['lookup_field']))  # noqa: E501
        if 'ordering' in params:
            query_params.append(('ordering', params['ordering']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/shortcuts/departments/tops/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
