from django.db import models


class Vip(models.Model):
    '''
    Vip模块
    '''
    name = models.CharField(max_length=32, unique=True)
    level = models.IntegerField()
    price = models.FloatField()

    def perms(self):
        '''
        当前vip具有的所有权限
        :return:
        '''
        rels = VipPermRelation.objects.filter(vip_id=self.id)
        perm_id_list = [rel.perm_id for rel in rels]
        return Permission.objects.filter(id__in=perm_id_list)

    def has_perm(self, perm_name):
        '''
        检查是否具有某种权限
        :param perm_name:
        :return:
        '''
        try:
            perm = Permission.objects.get(name=perm_name)
        except Permission.DoesNotExist:
            return False
        return VipPermRelation.objects.filter(vip_id=self.id, perm_id=perm.id).exists()


class Permission(models.Model):
    '''
    权限表：
        vipflag  会员身份标识  123
        superlike  超级喜欢  13
        rewind  反悔功能  23
        anylocation 任意更改定位  3
        unlimitlike  无限喜欢次数  23
    '''
    name = models.CharField(max_length=32, unique=True)


class VipPermRelation(models.Model):
    '''
    vip 权限 关系表
    '''
    vip_id = models.IntegerField()
    perm_id = models.IntegerField()
