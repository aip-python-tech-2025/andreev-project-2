class Category:
    def __init__(self, name):
        self.name = name
        self.requests = []

    def __repr__(self):
        return f'{self.name}'

    def __eq__(self, other):
        return isinstance(other, Category) and self.name == other.name

    def add_request(self, request):
        self.requests.append(request)
        print(request, "добавлена в категорию", self.name)
