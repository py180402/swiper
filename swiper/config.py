#-*- coding: utf-8 -*-
# @Time    : 2018/11/27 0027 14:39
# @Author  : zhyipeng
# @File    : config.py
# 第三方配置信息


# 互亿无线
HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': 'C72853033',
    'password': '83b6f8f330a26cf893a16193d837db25',
    'mobile': None,
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'format': 'json',
}

# 云之讯配置
SMS_SERVER_URL = 'https://open.ucpaas.com/ol/sms/sendsms'
SMS_PARAMS = {
    'sid': '04f8636fb94b42a523add5ce973e1b6e',
    'token': 'd281da517c99ae319acbfc1ce5dd0089',
    'appid': '0644843e19b4413fa9fb2efe3ee77801',
    'templateid': '402830',
    'param': None,
    'mobile': None,
}

# 七牛云
QN_ACCESS_KEY = ''
QN_SECRET_KEY = ''
QN_BUCKET_NAME = 'swiper'
QN_BASE_URL = 'http://...'