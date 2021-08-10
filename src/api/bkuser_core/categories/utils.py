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
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Callable, ContextManager, Iterator, Optional

from bkuser_core.categories.models import ProfileCategory

logger = logging.getLogger(__name__)


def change_category_type(category_id: int, target_type: str):
    """将其他类型的目录转换"""
    ins = ProfileCategory.objects.get(pk=category_id)

    logger.info(
        "going to change type of Category<%s> from %s to %s",
        ins.display_name,
        ins.type,
        target_type,
    )
    ins.type = target_type
    ins.save()


@dataclass
class TimeContext:
    start_time: float = field(default_factory=time.time)
    start_clock: float = field(default_factory=time.clock)
    end_time: Optional[float] = None
    end_clock: Optional[float] = None

    @property
    def time_delta(self):
        """消耗的时间"""
        if self.end_time is None:
            return time.time() - self.start_time
        return self.end_time - self.start_time

    @property
    def clock_delta(self):
        """消耗的 CPU 时钟"""
        if self.end_clock is None:
            return time.clock() - self.start_clock
        return self.end_clock - self.start_clock

    def close(self):
        self.end_time = time.time()
        self.end_clock = time.clock()


def __catch_time__() -> Iterator[TimeContext]:
    context = TimeContext()
    try:
        yield context
    finally:
        context.close()


catch_time: Callable[..., ContextManager[TimeContext]] = contextmanager(__catch_time__)
