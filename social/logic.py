#-*- coding: utf-8 -*-
# @Time    : 2018/11/29 0029 15:35
# @Author  : zhyipeng
# @File    : logic.py

import datetime

from user.models import *
from social.models import *


def get_rcmd_users(user):
    '''
    推荐算法
    :param user:
    :return:
    '''
    dating_sex = user.profile.dating_sex
    location = user.profile.location
    min_age = user.profile.min_dating_age
    max_age = user.profile.max_dating_age

    current_year = datetime.date.today().year
    max_year = current_year - min_age
    min_year = current_year - max_age
    print(max_year,min_year, location, dating_sex)
    users = User.objects.filter(sex=dating_sex, location=location, birth_year__range=(min_year, max_year))

    return users


def like(user, sid):
    '''
    喜欢一个用户
    :param user:
    :param sid:
    :return: 如果刚好匹配则返回True，否则False
    '''
    Swiped.mark(user.id, sid, 'like')
    # 检查被滑动用户是否喜欢过自己
    if Swiped.is_liked(sid, user.id):
        Friend.be_friends(user.id, sid)
        return True
    else:
        return False


def superlike(user, sid):
    '''
    超级喜欢一个用户
    :param user:
    :param sid:
    :return:
    '''
    Swiped.mark(user.id, sid, 'superlike')
    # 检查被滑动用户是否喜欢过自己
    if Swiped.is_liked(sid, user.id):
        Friend.be_friends(user.id, sid)
        return True
    else:
        return False


def dislike(user, sid):
    '''
    不喜欢一个用户
    :param user:
    :param sid:
    :return:
    '''
    Swiped.mark(user.id, sid, 'dislike')


def rewind(user, sid):
    '''
    反悔
    :param user:
    :param sid:
    :return:
    '''
    try:
        Swiped.objects.get(uid=user.id, sid=sid).delete()
    except Swiped.DoesNotExist:
        pass
    # 撤销好友关系
    Friend.break_off(user.id, sid)

