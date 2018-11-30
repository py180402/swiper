# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 0030 14:17
# @Author  : zhyipeng
# @File    : vip/logic.py
import logging

from lib.http import render_json
from .models import *
from common.error import NO_PERMISSION


log = logging.getLogger('err')

def perm_require(perm_name):
    '''
    权限检查装饰器
    :param perm_name: 权限名称
    :return:
    '''

    def deco(view_func):
        def wrap(request):
            user = request.user
            if user.vip.has_perm(perm_name):
                res = view_func(request)
                return res
            else:
                log.error(f'{user.nickname} not has {perm_name}')
                return render_json(None, NO_PERMISSION)
        return wrap

    return deco
