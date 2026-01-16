from core.service_request import ServiceRequest
from core.category import Category

request = ServiceRequest('Починить проектор', '2025-11-15', categories=[Category('Проекторы')])
print(request.title)
print(request.due_date)
print(request.is_due())
print(request)

another_request = ServiceRequest('Помыть доску', '2025-11-11', categories=[Category('Кабинет')])
clone = ServiceRequest('Починить проектор', '2025-11-15', categories=[Category('Проекторы')])

print(request == another_request)
print(request == clone)
