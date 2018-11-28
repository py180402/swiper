from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from user.models import User
from lib.http import render_json
from common.error import LOGIN_ERROR


class AuthMiddleware(MiddlewareMixin):
    '''
    用户登陆验证中间件
    '''
    WHITE_LIST = [
        'api/user/verify',
        'api/user/login',
    ]

    def process_request(self, request):
        # 跳过白名单
        # startswith 以xx开头
        for path in self.WHITE_LIST:
            if request.path.startswith(path):
                return
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
                return
            except User.DoesNotExist:
                request.session.flush()
        return render_json(None, code=LOGIN_ERROR)


class CorsMiddleware(MiddlewareMixin):
    '''处理客户端 JS 的跨域'''

    def process_request(self, request):
        if request.method == 'OPTIONS' and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = HttpResponse()
            response['Content-Length'] = '0'
            response['Access-Control-Allow-Headers'] = request.META['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']
            response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
            return response

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
