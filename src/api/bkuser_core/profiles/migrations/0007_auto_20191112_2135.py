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
# Generated by Django 1.11.23 on 2019-11-12 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0006_auto_20191111_2011"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="category_id",
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name="用户目录ID"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="domain",
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name="域"),
        ),
    ]
