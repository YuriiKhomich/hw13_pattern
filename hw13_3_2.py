'''

Cтворити об’єкт дії який при ініціалізації приймає 1 параметр text а при
виконанні виводить його
'''

class MyAction:
    def __call__(self):
        print("Hello World")

action = MyAction()

action()