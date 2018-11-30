from django.db import models
from django.db.models import Q
from user.models import User


class Swiped(models.Model):
    '''
    滑动记录
    '''
    STATUS = (
        ('superlike', '关注'),
        ('like', '喜欢'),
        ('dislike', '不喜欢')
    )
    # user_id
    uid = models.IntegerField(verbose_name='滑动者的id')
    # stranger_id
    sid = models.IntegerField(verbose_name='被滑动者的id')
    status = models.CharField(max_length=8, choices=STATUS)
    time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def mark(cls, uid, sid, status):
        '''
        标记一次滑动
        :param uid: user_id
        :param sid: strange_id
        :return:
        '''
        if status in ['superlike', 'like', 'dislike']:
            defaults = {'status': status}
            cls.objects.update_or_create(uid=uid, sid=sid, defaults=defaults)

    @classmethod
    def is_liked(cls, uid, sid):
        '''
        检查是user是否喜欢过某人
        :param uid: user_id
        :param sid: stranger_id
        :return: bool
        '''
        return cls.objects.filter(uid=uid, sid=sid, status__in=['like', 'superlike']).exists()


class Friend(models.Model):
    '''
    好友关系，User内部的多对多关系
    '''
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def be_friends(cls, uid1, uid2):
        '''
        新建一条朋友关系
        :param uid: user_id
        :param sid: stranger_id
        :return:
        '''
        uid1, uid2 = sorted([uid1, uid2])
        cls.objects.get_or_create(uid1=uid1, uid2=uid2)


    @classmethod
    def break_off(cls, uid1, uid2):
        '''
        断交
        :param uid1:
        :param uid2:
        :return:
        '''
        uid1, uid2 = sorted([uid1, uid2])
        try:
            cls.objects.get(uid1=uid1, uid2=uid2).delete()
        except cls.DoesNotExist:
            pass


    @classmethod
    def is_friend(cls, uid1, uid2):
        '''
        查询是否是好友
        :param uid1:
        :param uid2:
        :return: Bool
        '''
        condition = Q(uid1=uid1, uid2=uid2) | Q(uid1=uid2, uid2=uid1)
        return cls.objects.filter(condition).exists()


    @classmethod
    def friends(cls, uid):
        '''
        获取好友列表
        :param uid:
        :return:
        '''
        condition = Q(uid1=uid) | Q(uid2=uid)
        relations = cls.objects.filter(condition)
        # friend_id_list = [rel.uid1 if rel.uid2==uid else rel.uid2 for rel in relations]
        friend_id_list = [rel.uid1 + rel.uid2 - int(uid) for rel in relations]

        return User.objects.filter(id__in=friend_id_list)
