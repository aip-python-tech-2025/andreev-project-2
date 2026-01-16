from datetime import date


class ServiceRequest:
    def __init__(self, title, due_date=None, description='', categories=None):
        self.title = title
        self.due_date = due_date if due_date is not None else str(date.today())
        self.__description = description
        self.categories = categories or []
        self.__technicians = []
        self.__status = 'open'

    def __repr__(self):
        categories = ", ".join([str(c) for c in self.categories]) or "без категории"
        technicians = ", ".join([str(t) for t in self.__technicians]) or "не назначен"
        return "\n".join([
            self.title,
            f'Категории: {categories}',
            f'Срок: {self.due_date}',
            f'Исполнитель: {technicians}',
            f'Статус: {self.__status}',
        ])

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return (
            isinstance(other, ServiceRequest)
            and self.title == other.title
            and self.due_date == other.due_date
        )

    def get_description(self):
        return self.__description

    def add_technician(self, technician):
        self.__technicians.append(technician)

    def open(self):
        self.__status = 'open'

    def close(self):
        self.__status = 'closed'

    def is_open(self):
        return self.__status == 'open'

    def is_due(self):
        today = str(date.today())
        return self.due_date < today
