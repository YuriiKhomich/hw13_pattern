'''Сворити Класс User який може мати 3 статуси 1 standart 2 vip 3 super vip
В залежності від статусу користувача метод info буде виводити Ви vip ви
Звичайний корисутвач або Ви супер Vip корисутвач
'''


class User:
    def __init__(self, status):
        self.status = status
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def info(self):
        if self.strategy is not None:
            self.strategy.info()
        else:
            print("Невірний статус користувача")


class NormalUserStrategy:
    def info(self):
        print("Ви звичайний користувач")


class VIPUserStrategy:
    def info(self):
        print("Ви VIP користувач")


class SuperVIPUserStrategy:
    def info(self):
        print("Ви супер VIP користувач")



user1 = User(1)
user1.set_strategy(NormalUserStrategy())
user1.info()

user2 = User(2)
user2.set_strategy(VIPUserStrategy())
user2.info()

user3 = User(3)
user3.set_strategy(SuperVIPUserStrategy())
user3.info()
