import json

from django.http import HttpResponse
from lib.http import render_json
from user.models import *
from .logic import send_verify_code, check_vcode
from common.error import *


def get_verify_code(request):
    '''
    手机注册，获取验证码
    :param request:
    :return:
    '''
    phonenum = request.POST.get('phonenum')
    send_verify_code(phonenum)
    return render_json(None, 0)



def login(request):
    '''
    短信验证登陆
    :param request:
    :return:
    '''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum, vcode):
        user, _ = User.objects.get_or_create(phonenum=phonenum)
        request.session['uid'] = str(user.id)
        return render_json(user.to_dict(), 0)
    else:
        return render_json(None, VCODE_ERROR)


def get_profile(request):
    '''
    获取个人资料
    :param request:
    :return:
    '''

    pass


def modify_profile(request):
    '''
    修改个人资料
    :param request:
    :return:
    '''
    pass


def upload_avatar(request):
    '''
    头像上传
    :param request:
    :return:
    '''
    pass