"""
1.1 Створити класи Article Article2 Article3 Article4 Article5 Article6
Корисутвач має обрати 1 articel1 2 article2 і т д в залежності від вибору буде
в змінну article записаний об’єкт обраного класу вивести через print (Об’єкт)

"""


class Article:
    def __init__(self):
        self.title = "Article"

class Article2:
    def __init__(self):
        self.title = "Article2"

class Article3:
    def __init__(self):
        self.title = "Article3"

class Article4:
    def __init__(self):
        self.title = "Article4"

class Article5:
    def __init__(self):
        self.title = "Article5"

class Article6:
    def __init__(self):
        self.title = "Article6"

article_classes = {
    "1": Article,
    "2": Article2,
    "3": Article3,
    "4": Article4,
    "5": Article5,
    "6": Article6
}

choice = input("Виберіть статтю (1-6): ")

if choice in article_classes:
    article_class = article_classes[choice]
    article = article_class()
    print(article)
else:
    print("Неправильний вибір статті.")
