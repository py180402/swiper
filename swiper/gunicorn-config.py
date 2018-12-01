#-*- coding: utf-8 -*-
# @Time    : 2018/12/1 0001 14:41
# @Author  : zhyipeng
# @File    : gunicorn-config.py

import multiprocessing

bind = ["127.0.0.1:8000"]
daemon = True  # 是否开启守护进程模式
pidfile = 'gunicorn.pid'


workers = multiprocessing.cpu_count() * 2 + 1
# 指定一个异步处理的库
worker_class = "gevent"
worker_connections = 65535

keepalive = 60    # 服务器保持连接的时间，能够避免频繁的三次握手
timeout = 30
graceful_timeout = 10
forwarded_allow_ips = '*'

# 日志处理
capture_output = True
loglevel = 'info'
errorlog = 'logs/error.log'
