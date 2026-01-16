class User:
    def __init__(self, name, user_id):
        self._name = name
        self._id = user_id
        self.requests = []

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __repr__(self):
        return f'{self._name} (ID: {self._id})'

    def change_name(self, new_name: str):
        bad_words = ['дурак']
        if isinstance(new_name, str) and new_name.lower() not in bad_words:
            self._name = new_name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self.change_name(new_name)

    def add_request(self, request):
        self.requests.append(request)
        print(request, "создана пользователем", self._id)

    def close_request(self, request):
        request.close()
        print(request, "закрыта пользователем", self._id)

    def list_open_requests(self):
        requests_set = set(self.requests)
        for i in requests_set:
            if i.is_open():
                print(i)
