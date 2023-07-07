"""
1.2 Ствирити класи User User1 User2 User3 User4 User5 та списки
users1 users2 users3 users4 users5
Користувач обирає яким користувачем він бажає бути користувачем 1 2 3 4
або 5 далі в залежності від вибору буде створений об’єкт потрібного класу і
переміщений до відповідного списку User1 до списку users1 User2 до списку
users2 і т д
"""

class User:
    def __init__(self, name):
        self.name = name

class User1(User):
    pass

class User2(User):
    pass

class User3(User):
    pass

class User4(User):
    pass

class User5(User):
    pass

class UserFactory:
    user_types = {
        1: User1,
        2: User2,
        3: User3,
        4: User4,
        5: User5
    }

    @staticmethod
    def create_user(user_type, name):
        user_class = UserFactory.user_types.get(user_type)
        if user_class:
            return user_class(name)
        else:
            raise ValueError("Invalid user type")

users1 = []
users2 = []
users3 = []
users4 = []
users5 = []

user_choice = int(input("Оберіть користувача (1, 2, 3, 4 або 5): "))
user_factory = UserFactory()
user = user_factory.create_user(user_choice, "Ім'я користувача")

users_dict = {
    1: users1,
    2: users2,
    3: users3,
    4: users4,
    5: users5
}
users_dict.get(user_choice, []).append(user)

print(f"Створений об'єкт користувача: {user}")
