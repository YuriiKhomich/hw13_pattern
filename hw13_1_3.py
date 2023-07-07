"""
1.3 Створити об’єкти Car Phone User з полями за Вашим баченням
(обов’язково хоча б одне приватне) Надати кожному функціонал по створені
копії об’єкта який викликає метод copy
"""
import copy

class CopyMixin:
    def copy(self):
        return copy.deepcopy(self)

class CarPhoneUser(CopyMixin):
    def __init__(self, name, car_model, phone_model):
        self._name = name
        self._car_model = car_model
        self._phone_model = phone_model

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_car_model(self):
        return self._car_model

    def set_car_model(self, car_model):
        self._car_model = car_model

    def get_phone_model(self):
        return self._phone_model

    def set_phone_model(self, phone_model):
        self._phone_model = phone_model


# Приклад використання
user1 = CarPhoneUser("Юрий", "Ситроен", "Самсунг")
print(user1.get_name())
print(user1.get_car_model())
print(user1.get_phone_model())

user2 = user1.copy()
user2.set_name("Юрий2")
user2.set_car_model("Смарт")
user2.set_phone_model("Samsung")

print(user2.get_name())
print(user2.get_car_model())
print(user2.get_phone_model())

print(user1.get_name())
print(user1.get_car_model())
print(user1.get_phone_model())
