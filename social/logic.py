#-*- coding: utf-8 -*-
# @Time    : 2018/11/29 0029 15:35
# @Author  : zhyipeng
# @File    : logic.py

import datetime

from user.models import *


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

    users = User.objects.filter(sex=dating_sex, location=location, birth_year__range=(min_year, max_year))

    return users