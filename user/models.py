from django.db import models
import datetime

from django.utils.functional import cached_property


class User(models.Model):
    '''
    用户数据模型
    '''
    # 第一项是记录到数据库里的值，第二项是描述
    SEX = (
        ('男', '男'),
        ('女', '女'),
    )

    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=32, unique=True)

    sex = models.CharField(max_length=8,default='男', choices=SEX)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    # 头像
    avatar = models.CharField(max_length=256)
    # 长居地
    location = models.CharField(max_length=32)

    # cached_property缓存功能，不用每次都计算
    @cached_property
    def age(self):
        now = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (now - birth_date).days // 365

    @property
    def profile(self):
        # 避免使用外键，手动构建关联，使id相等（一对一）
        # 动态绑定_profile属性，避免频繁访问数据库
        # if '_profile' not in self.__dict__:
        # hasattr 检查对象是否有某个属性
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile


class Profile(models.Model):
    '''
    用户配置项
    '''
    SEX = (
        ('男', '男'),
        ('女', '女'),
    )

    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大交友年龄')

    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=45, verbose_name='最大交友年龄')

    dating_sex = models.CharField(max_length=8, choices=SEX, default='女', verbose_name='匹配性别')

    vibration = models.BooleanField(default=True, verbose_name='是否开始震动')
    only_matche = models.BooleanField(default=False, verbose_name='不让未匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='是否自动播放视频')
