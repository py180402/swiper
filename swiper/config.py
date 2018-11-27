#-*- coding: utf-8 -*-
# @Time    : 2018/11/27 0027 14:39
# @Author  : zhyipeng
# @File    : config.py
# 第三方配置信息

# APIID: C72853033
# APIKEY: 83b6f8f330a26cf893a16193d837db25


HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': 'C72853033',
    'password': '83b6f8f330a26cf893a16193d837db25',
    'mobile': None,
    'content': '您的验证码是：%。请不要把验证码泄露给其他人。',
    'format': 'json',
}