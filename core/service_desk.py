class ServiceDesk:
    @staticmethod
    def get_request_by_title(title):
        requests = [
            {'title': 'Сгорел комп', 'category': 'Компьютеры', 'status': 'open'},
            {'title': 'Не работает принтер', 'category': 'Оргтехника', 'status': 'open'},
        ]
        for item in requests:
            if item['title'] == title:
                return item
        return None
