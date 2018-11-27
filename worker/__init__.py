# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 0027 15:58
# @Author  : zhyipeng
# @File    : __init__.py.py
# celery 模块

import os
from celery import Celery

# 设置环境变量，加载django的settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')

# 创建 Celery Application
celery_app = Celery('swiper')
celery_app.config_from_object('worker.config')
celery_app.autodiscover_tasks()


def call_by_worker(func):
    '''
    将任务在Celery中异步执行
    :param func:
    :return:
    '''
    # 手动执行装饰器
    task = celery_app.task(func)
    return task.delay
