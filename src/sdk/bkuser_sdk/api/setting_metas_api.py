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


class SettingMetasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v2_setting_metas_create(self, body, **kwargs):  # noqa: E501
        """v2_setting_metas_create  # noqa: E501

        配置信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingMeta body: (required)
        :return: SettingMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_setting_metas_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_setting_metas_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v2_setting_metas_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """v2_setting_metas_create  # noqa: E501

        配置信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingMeta body: (required)
        :return: SettingMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_setting_metas_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v2_setting_metas_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/setting_metas/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingMeta',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_setting_metas_delete(self, lookup_value, **kwargs):  # noqa: E501
        """v2_setting_metas_delete  # noqa: E501

        删除对象  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_delete(lookup_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lookup_value: (required)
        :param str fields: 指定对象返回字段，支持多选，以逗号分隔，例如: username,status,id
        :param str lookup_field: 指定查询字段，内容为 lookup_value 所属字段, 例如: username
        :param bool include_disabled: 是否包含已软删除的数据
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_setting_metas_delete_with_http_info(lookup_value, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_setting_metas_delete_with_http_info(lookup_value, **kwargs)  # noqa: E501
            return data

    def v2_setting_metas_delete_with_http_info(self, lookup_value, **kwargs):  # noqa: E501
        """v2_setting_metas_delete  # noqa: E501

        删除对象  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_delete_with_http_info(lookup_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lookup_value: (required)
        :param str fields: 指定对象返回字段，支持多选，以逗号分隔，例如: username,status,id
        :param str lookup_field: 指定查询字段，内容为 lookup_value 所属字段, 例如: username
        :param bool include_disabled: 是否包含已软删除的数据
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lookup_value', 'fields', 'lookup_field', 'include_disabled']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_setting_metas_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lookup_value' is set
        if ('lookup_value' not in params or
                params['lookup_value'] is None):
            raise ValueError("Missing the required parameter `lookup_value` when calling `v2_setting_metas_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lookup_value' in params:
            path_params['lookup_value'] = params['lookup_value']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'lookup_field' in params:
            query_params.append(('lookup_field', params['lookup_field']))  # noqa: E501
        if 'include_disabled' in params:
            query_params.append(('include_disabled', params['include_disabled']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/setting_metas/{lookup_value}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_setting_metas_list(self, **kwargs):  # noqa: E501
        """v2_setting_metas_list  # noqa: E501

        获取对象列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ordering: Which field to use when ordering the results.
        :param int page: A page number within the paginated result set.
        :param int page_size: Number of results to return per page.
        :param list[str] fields: 指定对象返回字段，支持多选，以逗号分隔，例如: username,status,id
        :param str lookup_field: 查询字段，针对 exact_lookups,fuzzy_lookups 生效
        :param list[str] exact_lookups: 精确查询 lookup_field 所指定的字段, 支持多选，以逗号分隔，例如: cat,dog,fish
        :param list[str] fuzzy_lookups: 模糊查询 lookup_field 所指定的字段, 支持多选，以逗号分隔，例如: cat,dog,fish
        :param str wildcard_search: 在多个字段模糊搜索的内容
        :param list[str] wildcard_search_fields: 指定多个模糊搜索字段
        :param bool best_match: 是否按照最短匹配排序
        :param str time_field: 时间过滤字段，支持 update_time, create_time
        :param datetime since: 筛选某个时间点后的记录
        :param datetime until: 筛选某个时间点前的记录
        :param bool include_disabled: 是否包含已软删除的数据
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_setting_metas_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_setting_metas_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_setting_metas_list_with_http_info(self, **kwargs):  # noqa: E501
        """v2_setting_metas_list  # noqa: E501

        获取对象列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ordering: Which field to use when ordering the results.
        :param int page: A page number within the paginated result set.
        :param int page_size: Number of results to return per page.
        :param list[str] fields: 指定对象返回字段，支持多选，以逗号分隔，例如: username,status,id
        :param str lookup_field: 查询字段，针对 exact_lookups,fuzzy_lookups 生效
        :param list[str] exact_lookups: 精确查询 lookup_field 所指定的字段, 支持多选，以逗号分隔，例如: cat,dog,fish
        :param list[str] fuzzy_lookups: 模糊查询 lookup_field 所指定的字段, 支持多选，以逗号分隔，例如: cat,dog,fish
        :param str wildcard_search: 在多个字段模糊搜索的内容
        :param list[str] wildcard_search_fields: 指定多个模糊搜索字段
        :param bool best_match: 是否按照最短匹配排序
        :param str time_field: 时间过滤字段，支持 update_time, create_time
        :param datetime since: 筛选某个时间点后的记录
        :param datetime until: 筛选某个时间点前的记录
        :param bool include_disabled: 是否包含已软删除的数据
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ordering', 'page', 'page_size', 'fields', 'lookup_field', 'exact_lookups', 'fuzzy_lookups', 'wildcard_search', 'wildcard_search_fields', 'best_match', 'time_field', 'since', 'until', 'include_disabled']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_setting_metas_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ordering' in params:
            query_params.append(('ordering', params['ordering']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'lookup_field' in params:
            query_params.append(('lookup_field', params['lookup_field']))  # noqa: E501
        if 'exact_lookups' in params:
            query_params.append(('exact_lookups', params['exact_lookups']))  # noqa: E501
            collection_formats['exact_lookups'] = 'csv'  # noqa: E501
        if 'fuzzy_lookups' in params:
            query_params.append(('fuzzy_lookups', params['fuzzy_lookups']))  # noqa: E501
            collection_formats['fuzzy_lookups'] = 'csv'  # noqa: E501
        if 'wildcard_search' in params:
            query_params.append(('wildcard_search', params['wildcard_search']))  # noqa: E501
        if 'wildcard_search_fields' in params:
            query_params.append(('wildcard_search_fields', params['wildcard_search_fields']))  # noqa: E501
            collection_formats['wildcard_search_fields'] = 'csv'  # noqa: E501
        if 'best_match' in params:
            query_params.append(('best_match', params['best_match']))  # noqa: E501
        if 'time_field' in params:
            query_params.append(('time_field', params['time_field']))  # noqa: E501
        if 'since' in params:
            query_params.append(('since', params['since']))  # noqa: E501
        if 'until' in params:
            query_params.append(('until', params['until']))  # noqa: E501
        if 'include_disabled' in params:
            query_params.append(('include_disabled', params['include_disabled']))  # noqa: E501

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
            '/api/v2/setting_metas/', 'GET',
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

    def v2_setting_metas_partial_update(self, body, lookup_value, **kwargs):  # noqa: E501
        """v2_setting_metas_partial_update  # noqa: E501

        配置信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_partial_update(body, lookup_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingMeta body: (required)
        :param str lookup_value: (required)
        :return: SettingMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_setting_metas_partial_update_with_http_info(body, lookup_value, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_setting_metas_partial_update_with_http_info(body, lookup_value, **kwargs)  # noqa: E501
            return data

    def v2_setting_metas_partial_update_with_http_info(self, body, lookup_value, **kwargs):  # noqa: E501
        """v2_setting_metas_partial_update  # noqa: E501

        配置信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_partial_update_with_http_info(body, lookup_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingMeta body: (required)
        :param str lookup_value: (required)
        :return: SettingMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'lookup_value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_setting_metas_partial_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v2_setting_metas_partial_update`")  # noqa: E501
        # verify the required parameter 'lookup_value' is set
        if ('lookup_value' not in params or
                params['lookup_value'] is None):
            raise ValueError("Missing the required parameter `lookup_value` when calling `v2_setting_metas_partial_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lookup_value' in params:
            path_params['lookup_value'] = params['lookup_value']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/setting_metas/{lookup_value}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingMeta',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_setting_metas_read(self, lookup_value, **kwargs):  # noqa: E501
        """v2_setting_metas_read  # noqa: E501

        获取详细信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_read(lookup_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lookup_value: (required)
        :param str fields: 指定对象返回字段，支持多选，以逗号分隔，例如: username,status,id
        :param str lookup_field: 指定查询字段，内容为 lookup_value 所属字段, 例如: username
        :param bool include_disabled: 是否包含已软删除的数据
        :return: SettingMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_setting_metas_read_with_http_info(lookup_value, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_setting_metas_read_with_http_info(lookup_value, **kwargs)  # noqa: E501
            return data

    def v2_setting_metas_read_with_http_info(self, lookup_value, **kwargs):  # noqa: E501
        """v2_setting_metas_read  # noqa: E501

        获取详细信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_read_with_http_info(lookup_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lookup_value: (required)
        :param str fields: 指定对象返回字段，支持多选，以逗号分隔，例如: username,status,id
        :param str lookup_field: 指定查询字段，内容为 lookup_value 所属字段, 例如: username
        :param bool include_disabled: 是否包含已软删除的数据
        :return: SettingMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lookup_value', 'fields', 'lookup_field', 'include_disabled']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_setting_metas_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lookup_value' is set
        if ('lookup_value' not in params or
                params['lookup_value'] is None):
            raise ValueError("Missing the required parameter `lookup_value` when calling `v2_setting_metas_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lookup_value' in params:
            path_params['lookup_value'] = params['lookup_value']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'lookup_field' in params:
            query_params.append(('lookup_field', params['lookup_field']))  # noqa: E501
        if 'include_disabled' in params:
            query_params.append(('include_disabled', params['include_disabled']))  # noqa: E501

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
            '/api/v2/setting_metas/{lookup_value}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingMeta',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_setting_metas_update(self, body, lookup_value, **kwargs):  # noqa: E501
        """v2_setting_metas_update  # noqa: E501

        更新对象  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_update(body, lookup_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingMeta body: (required)
        :param str lookup_value: (required)
        :param str fields: 指定对象返回字段，支持多选，以逗号分隔，例如: username,status,id
        :param str lookup_field: 指定查询字段，内容为 lookup_value 所属字段, 例如: username
        :param bool include_disabled: 是否包含已软删除的数据
        :return: SettingMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_setting_metas_update_with_http_info(body, lookup_value, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_setting_metas_update_with_http_info(body, lookup_value, **kwargs)  # noqa: E501
            return data

    def v2_setting_metas_update_with_http_info(self, body, lookup_value, **kwargs):  # noqa: E501
        """v2_setting_metas_update  # noqa: E501

        更新对象  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_setting_metas_update_with_http_info(body, lookup_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingMeta body: (required)
        :param str lookup_value: (required)
        :param str fields: 指定对象返回字段，支持多选，以逗号分隔，例如: username,status,id
        :param str lookup_field: 指定查询字段，内容为 lookup_value 所属字段, 例如: username
        :param bool include_disabled: 是否包含已软删除的数据
        :return: SettingMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'lookup_value', 'fields', 'lookup_field', 'include_disabled']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_setting_metas_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v2_setting_metas_update`")  # noqa: E501
        # verify the required parameter 'lookup_value' is set
        if ('lookup_value' not in params or
                params['lookup_value'] is None):
            raise ValueError("Missing the required parameter `lookup_value` when calling `v2_setting_metas_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lookup_value' in params:
            path_params['lookup_value'] = params['lookup_value']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'lookup_field' in params:
            query_params.append(('lookup_field', params['lookup_field']))  # noqa: E501
        if 'include_disabled' in params:
            query_params.append(('include_disabled', params['include_disabled']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/setting_metas/{lookup_value}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingMeta',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
