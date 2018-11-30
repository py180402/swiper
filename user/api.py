import json
import os

from lib.http import render_json
from user.models import *
from .logic import send_verify_code, check_vcode, save_upload_file
from common.error import *
from .forms import ProfileForm


def get_verify_code(request):
    '''
    手机注册，获取验证码
    :param request:
    :return:
    '''
    phonenum = request.POST.get('phonenum')
    print(phonenum)
    send_verify_code(phonenum)
    return render_json(None)


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
        return render_json(user.to_dict())
    else:
        return render_json(None, VCODE_ERROR)


def get_profile(request):
    '''
    获取个人资料
    :param request:
    :return:
    '''
    user = request.user
    return render_json(user.profile.to_dict())


def modify_profile(request):
    '''
    修改个人资料
    :param request:
    :return:
    '''
    form = ProfileForm(request.POST)
    if form.is_valid():
        user = request.user
        user.profile.__dict__.update(form.cleaned_data)
        user.profile.save()
        return render_json(None)
    else:
        return render_json(form.errors, PROFILE_ERROR)


def upload_avatar(request):
    '''
    头像上传
    :param request:
    :return:
    '''
    # 接受用户上传的头像
    # 定义头像名称
    file = request.FILES.get('avatar')
    if file is None:
        return render_json(None, FILE_NOT_FOUND)
    # 保存到本地且异步上传到七牛
    # 将url保存入数据库
    save_upload_file(file, request.user)
    return render_json(None)
