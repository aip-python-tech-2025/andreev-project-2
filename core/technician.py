from core.user import User


class Technician(User):
    def __init__(self, name, business_days, user_id):
        super().__init__(name, user_id)
        self.__business_days = business_days

    def __repr__(self):
        return f'{super().__repr__()}, рабочие дни: {self.__business_days}'
