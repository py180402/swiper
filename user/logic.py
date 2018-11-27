# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 0027 14:34
# @Author  : zhyipeng
# @File    : logic.py
# 一些逻辑处理
import requests
import random
from swiper import config
from worker import call_by_worker
from django.core.cache import cache


def gen_verify_code(length=6):
    '''
    生成验证码
    :param length: 验证码长度
    :return: 验证码，str
    '''
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])


@call_by_worker
def send_verify_code(phonenum):
    '''
    发送验证码短信
    :param phonenum: 手机号, str
    :return: json
    '''
    code = gen_verify_code()
    key = 'VerifyCode-%s' % phonenum
    # 存入缓存
    cache.set(key, code, timeout=120)

    data = config.HY_SMS_PARAMS.copy()
    data['content'] = data['content'] % code
    data['mobile'] = phonenum

    response = requests.post(url=config.HY_SMS_URL, data=data)
    return response.json()
