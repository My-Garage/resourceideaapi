"""Logging systems"""


class ConsoleLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print('TIMESTAMP:', request.timestamp, 'USER:', request.user)
        return response
