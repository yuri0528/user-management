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
import logging
from typing import TYPE_CHECKING

from django.conf import settings

if TYPE_CHECKING:
    from django.http.request import HttpRequest

logger = logging.getLogger(__name__)


def need_iam(request: "HttpRequest") -> bool:
    """是否需要权限中心"""
    if not settings.ENABLE_IAM:
        return False

    if settings.NEED_IAM_HEADER not in request.META:
        return False

    return bool(request.META[settings.NEED_IAM_HEADER])
