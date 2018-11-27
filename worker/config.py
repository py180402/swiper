#-*- coding: utf-8 -*-
# @Time    : 2018/11/27 0027 15:58
# @Author  : zhyipeng
# @File    : config.py
# celery 配置

broker_url = 'redis://127.0.0.1:6379/0'
broker_pool_limit = 1000

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']

task_serializer = 'pickle'
result_expires = 3600

result_backend = 'redis://127.0.0.1:6379/0'
result_serializer = 'pickle'
result_cache_max = 10000

worker_redirect_stdouts_level = 'INFO'