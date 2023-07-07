'''
2.3 Наявний список data
Необхідно створити функції action action2 action3 кожна з яких буде
виводити інформацію про те яка це функція наприклад action напис “це
action1” і відповідно таке саме до action2 action3 Необхідно модивікувати

функції таким чином аби вони виводили інформацію про себе тільки тоді
коли в списку data хоч щось є і іншому випадку напис Виконати неможливо
'''

import functools


class FunctionDecorator:
    def __init__(self, func):
        functools.wraps(func)(self)
        self.func = func
    
    def __call__(self):
        if data:
            print(f"Це {self.__name__}")
            self.func()
        else:
            print("Выполнить невозможно")


@FunctionDecorator
def action():
    print("Выполняется action")


@FunctionDecorator
def action2():
    print("Выполняется action2")


@FunctionDecorator
def action3():
    print("Выполняется action3")


# Пример
data = [1, 2, 3]
action2()

data = [3]
action()

data = []
action3()