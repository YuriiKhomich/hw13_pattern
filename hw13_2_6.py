'''
2.5 Створити Класс Товар (поля за Власним бажанням)
Адміністратор може створювати товари
Користувач може додати в кошик товари зазначаючи скільлки він їх придбав
'''

class Worker:
    def __init__(self, title, phone, position, name):
        self.title = title
        self.phone = phone
        self.position = position
        self.name = name


worker1 = Worker("worker", "123-123-21-21", "Менеджер", "Юрий")
worker2 = Worker("worker", "124-124-22-22", "Менеджер", "Вася")
workers = [worker1, worker2]


class CallRecord:
    def __init__(self, call_number, phone, position, name, worker_number):
        self.call_number = call_number
        self.phone = phone
        self.position = position
        self.name = name
        self.worker_number = worker_number
    
    @property
    def worker(self):
        return workers[self.worker_number]


records = [
    CallRecord(1, worker1.phone, worker1.position, worker1.name, 0),
    CallRecord(2, worker2.phone, worker2.position, worker2.name, 1),
    CallRecord(3, worker2.phone, worker2.position, worker2.name, 1),
    CallRecord(4, worker1.phone, worker1.position, worker1.name, 0),
    CallRecord(5, worker1.phone, worker1.position, worker1.name, 0),
    CallRecord(6, worker1.phone, worker1.position, worker1.name, 0),
    CallRecord(7, worker1.phone, worker1.position, worker1.name, 0)
]

record = records[2]
print(record.worker.name)
