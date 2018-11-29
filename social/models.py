from django.db import models


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
            cls.objects.create(uid=uid, sid=sid, status=status)

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
        cls.objects.create(uid1=uid1, uid2=uid2)