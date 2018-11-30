import logging

from lib.http import render_json
from .models import *
from social import logic
from vip.logic import perm_require

log = logging.getLogger('inf')


def users(request):
    '''
    获取推荐列表
    :param request:
    :return:
    '''

    page = int(request.POST.get('page', 1))
    limit = int(request.POST.get('limit', 5))
    users = logic.get_rcmd_users(request.user)[(page - 1) * limit: page * limit]

    result = [user.to_dict() for user in users]

    return render_json(result)


def like(request):
    '''
    喜欢
    :param request:
    :return:
    '''
    sid = int(request.POST.get('sid'))
    is_matched = logic.like(request.user, sid)
    log.info(f'{request.user.id} like {sid}')
    return render_json({'is_matched': is_matched})


@perm_require('superlike')
def superlike(request):
    '''
    超级喜欢
    :param request:
    :return:
    '''
    sid = int(request.POST.get('sid'))
    is_matched = logic.superlike(request.user, sid)
    log.info(f'{request.user.id} superlike {sid}')
    return render_json({'is_matched': is_matched})


def dislike(request):
    '''
    不喜欢
    :param request:
    :return:
    '''
    sid = int(request.POST.get('sid'))
    logic.dislike(request.user, sid)
    log.info(f'{request.user.id} dislike {sid}')
    return render_json(None)


@perm_require('rewind')
def rewind(request):
    '''
    反悔
    :param request:
    :return:
    '''
    sid = request.POST.get('sid')
    logic.rewind(request.user, sid)
    return render_json(None)


def friends(request):
    '''
    获取好友列表
    :param request:
    :return:
    '''
    my_friends = Friend.friends(request.user.id)
    friends_info = [f.to_dict() for f in my_friends]
    return render_json({'friends': friends_info})
