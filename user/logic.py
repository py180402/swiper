# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 0027 14:34
# @Author  : zhyipeng
# @File    : logic.py
# 一些逻辑处理
import os

import requests
import random
from urllib.parse import urljoin
from django.core.cache import cache
from django.conf import settings
from lib.qncloud import async_upload_to_qiniu
from swiper import config
from worker import call_by_worker


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
    发送验证码短信，异步
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


def check_vcode(phonenum, vcode):
    '''
    检查验证码是否正确
    :param phonenum: 手机号
    :param vcode: 用户提交的验证码
    :return: Bool
    '''
    key = 'VerifyCode-%s' % phonenum
    saved_vcode = cache.get(key)
    return saved_vcode == vcode


def save_upload_file(upload_file, user):
    '''
    保存用户上传的文件到本地、七牛云和数据库
    :param file:
    :return:
    '''
    filename = 'Avatar-%s%s' % (user.id, os.path.splitext(upload_file.name)[1])
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    with open(filepath, 'wb') as f:
        for chunk in upload_file.chunks():
            f.write(chunk)

    ret, info = async_upload_to_qiniu(filepath, filename)
    url = urljoin(config.QN_BASE_URL, filename)
    user.avatar = url
    user.save()
