from lib.http import render_json
from .models import *
from .logic import get_rcmd_users


def users(request):
    '''
    获取推荐列表
    :param request:
    :return:
    '''

    page = int(request.POST.get('page', 1))
    limit = int(request.POST.get('limit', 5))
    users = get_rcmd_users(request.user)[(page-1)*limit, page*limit]

    result = [user.to_dict() for user in users]

    return render_json(result)


def like(request):
    '''
    喜欢
    :param request:
    :return:
    '''
    pass

def superlike(request):
    '''
    关注
    :param request:
    :return:
    '''
    pass

def dislike(request):
    '''
    不喜欢
    :param request:
    :return:
    '''
    pass

def rewind(request):
    '''
    返回
    :param request:
    :return:
    '''
    pass