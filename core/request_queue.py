from .service_request import ServiceRequest


class RequestQueue:
    def __init__(self, name):
        self.__name = name
        self.__requests = []

    def add_request(self, request):
        if isinstance(request, ServiceRequest):
            self.__requests.append(request)

    def __repr__(self):
        return f'{self.__name} (всего заявок: {len(self.__requests)})'
