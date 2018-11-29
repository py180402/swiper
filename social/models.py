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


class Friend(models.Model):
    '''
    好友关系，User内部的多对多关系
    '''
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()