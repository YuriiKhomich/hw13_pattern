'''
1.4 Створити клас Config з полями field1 field2 field3 при зміні полів в одному
об’єкті мають змінюватись поля у всіх об’єктах цього класу
'''

class Config:
    _instance = None
    field1 = None
    field2 = None
    field3 = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, field1=None, field2=None, field3=None):
        if field1 is not None:
            Config.field1 = field1
        if field2 is not None:
            Config.field2 = field2
        if field3 is not None:
            Config.field3 = field3

    def update_fields(self, field1=None, field2=None, field3=None):
        if field1 is not None:
            Config.field1 = field1
        if field2 is not None:
            Config.field2 = field2
        if field3 is not None:
            Config.field3 = field3


config1 = Config()
print(config1.field1)

config1.update_fields(field1="Value 1")

config2 = Config()
print(config2.field1)
config2.update_fields(field1="New Value")
print(config1.field1)
