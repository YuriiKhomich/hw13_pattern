'''
Створити нескінченну послідовність від – 1000 до 1000
Спочатку від -1000 виводить числа до 1000 як тільки доходить до 1000
починає повертати числа в зворотньому порядку
Тобто
-1000 -999 -998 ……..0 1 2 3……. 1000 999 998 997 ….0 …… -1 -2 -3 …..-
1000 -999 і т д
'''

class MyData:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.direction = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.start

        if self.start == self.stop and self.direction == 1:
            self.direction = -1
        elif self.start == -self.stop and self.direction == -1:
            self.direction = 1

        self.start += self.direction

        return result

my_data = MyData(-1000, 1000)
while True:
    value = next(my_data)
    print(value)
