#!/usr/bin/env python

import os
import sys
import random

import django

# 设置环境

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BACKEND_DIR = os.path.join(BASE_DIR, 'backend')

sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")
django.setup()

from user.models import User
from vip.models import Permission, Vip, VipPermRelation


last_names = (
    '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨'
    '朱秦尤许何吕施张孔曹严华金魏陶姜'
    '戚谢邹喻柏水窦章云苏潘葛奚范彭郎'
    '鲁韦昌马苗凤花方俞任袁柳酆鲍史唐'
    '费廉岑薛雷贺倪汤滕殷罗毕郝邬安常'
    '乐于时傅皮卞齐康伍余元卜顾孟平黄'
)

first_names = {
    '男': [
        '致远', '俊驰', '雨泽', '烨磊', '晟睿',
        '天佑', '文昊', '修洁', '黎昕', '远航',
        '旭尧', '鸿涛', '伟祺', '荣轩', '越泽',
        '浩宇', '瑾瑜', '皓轩', '浦泽', '绍辉',
        '绍祺', '升荣', '圣杰', '晟睿', '思聪'
    ],
    '女': [
        '沛玲', '欣妍', '佳琦', '雅芙', '雨婷',
        '韵寒', '莉姿', '雨婷', '宁馨', '妙菱',
        '心琪', '雯媛', '诗婧', '露洁', '静琪',
        '雅琳', '灵韵', '清菡', '溶月', '素菲',
        '雨嘉', '雅静', '梦洁', '梦璐', '惠茜'
    ]
}


def rand_name():
    last_name = random.choice(last_names)
    sex = random.choice(['男', '女'])
    first_name = random.choice(first_names[sex])
    return ''.join([last_name, first_name]), sex


# 创建初始用户
def create_robots(n):
    for i in range(n):
        name, sex = rand_name()
        try:
            User.objects.create(
                phonenum='%s' % random.randrange(21000000000, 21900000000),
                nickname=name,
                sex=sex,
                birth_year=random.randint(1980, 2000),
                birth_month=random.randint(1, 12),
                birth_day=random.randint(1, 28),
                location=random.choice(['北京', '上海', '深圳', '成都', '西安', '沈阳', '武汉']),
            )
        except:
            continue
        print('created: %s %s' % (name, sex))


def init_permission():
    '''
    创建权限模型
    :return:
    '''
    '''
    权限表：
        vipflag    会员身份标识  123
        superlike  超级喜欢  13
        rewind     反悔功能  23
        anylocation 任意更改定位  3
        unlimitlike  无限喜欢次数  23
    '''
    permission_names = ['vipflag',
                        'superlike',
                        'rewind',
                        'anylocation',
                        'unlimitlike', ]
    for name in permission_names:
        Permission.objects.get_or_create(name=name)


def init_vip():
    '''
    创建vip模型
    :return:
    '''
    for i in range(4):
        Vip.objects.get_or_create(
            name='vip%d' % i,
            level=i,
            price=i * 10.0
        )


def create_vip_perm_relations():
    '''
    创建vip 和 permission 的关系
    :return:
    '''
    vip1, _ = Vip.objects.get_or_create(level=1)
    vip2, _ = Vip.objects.get_or_create(level=2)
    vip3, _ = Vip.objects.get_or_create(level=3)
    vipflag = Permission.objects.get(name='vipflag')
    superlike = Permission.objects.get(name='superlike')
    rewind = Permission.objects.get(name='rewind')
    anylocation = Permission.objects.get(name='anylocation')
    unlimitlike = Permission.objects.get(name='unlimitlike')

    VipPermRelation.objects.get_or_create(vip_id=vip1.id, perm_id=vipflag.id)
    VipPermRelation.objects.get_or_create(vip_id=vip1.id, perm_id=superlike.id)

    VipPermRelation.objects.get_or_create(vip_id=vip2.id, perm_id=vipflag.id)
    VipPermRelation.objects.get_or_create(vip_id=vip2.id, perm_id=rewind.id)

    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=vipflag.id)
    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=superlike.id)
    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=rewind.id)
    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=anylocation.id)
    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=unlimitlike.id)



if __name__ == '__main__':
    # create_robots(1000)
    init_vip()
    init_permission()
    create_vip_perm_relations()