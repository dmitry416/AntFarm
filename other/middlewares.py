from django.conf.global_settings import SESSION_COOKIE_NAME
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        if request.path == '/telauth/':
            return self.get_response(request)

        if SESSION_COOKIE_NAME not in request.COOKIES and 'hash' not in request.GET:
            return redirect('auth')

        return self.get_response(request)
