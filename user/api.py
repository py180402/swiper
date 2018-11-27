from user.models import *
from .logic import send_verify_code


def get_verify_code(request):
    '''
    手机注册，获取验证码
    :param request:
    :return:
    '''
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)



def login(request):
    '''
    短信验证登陆
    :param request:
    :return:
    '''
    pass


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