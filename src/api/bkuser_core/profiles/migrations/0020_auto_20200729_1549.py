# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-用户管理(Bk-User) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
# Generated by Django 1.11.23 on 2020-07-29 07:49
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    """添加内建字段信息"""
    DynamicFieldInfo = apps.get_model("profiles", "DynamicFieldInfo")

    builtin_fields_info = dict(
        username=dict(display_name="用户名", display_name_en="Username", display_name_zh_hans="用户名"),
        display_name=dict(display_name="全名", display_name_en="DisplayName", display_name_zh_hans="全名"),
        email=dict(display_name="邮箱", display_name_en="Email", display_name_zh_hans="邮箱"),
        telephone=dict(display_name="手机号", display_name_en="Telephone", display_name_zh_hans="手机号"),
        status=dict(
            display_name="账户状态",
            display_name_en="AccountStatus",
            display_name_zh_hans="账户状态",
        ),
        staff_status=dict(
            display_name="在职状态",
            display_name_en="StaffStatus",
            display_name_zh_hans="在职状态",
        ),
        department_name=dict(display_name="组织", display_name_en="Departments", display_name_zh_hans="组织"),
        leader=dict(display_name="上级", display_name_en="Leaders", display_name_zh_hans="上级"),
        position=dict(display_name="职务", display_name_en="Position", display_name_zh_hans="职务"),
        wx_userid=dict(display_name="微信", display_name_en="Wechat", display_name_zh_hans="微信"),
        qq=dict(display_name="QQ", display_name_en="QQ", display_name_zh_hans="QQ"),
    )

    for k, info in builtin_fields_info.items():
        DynamicFieldInfo.objects.filter(name=k).update(**info)

    for d in DynamicFieldInfo.objects.filter(builtin=False):
        d.display_name_en = d.display_name_zh_hans = d.display_name
        d.save(update_fields=["display_name_en", "display_name_zh_hans"])


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0019_auto_20200729_1543"),
    ]

    operations = [migrations.RunPython(forwards_func)]
