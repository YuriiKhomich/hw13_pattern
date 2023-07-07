'''
2.1 Створити Клас Користувач Який має приймати один із декількох
можливих наборів параметрів:
1 Набір Адміністратор з полями admin_field1 admin_field2
2 Набір Користувач підтримки з полями support_field1 support_field2
'''
class AdminUser:
    def __init__(self, admin_field1, admin_field2):
        self.admin_field1 = admin_field1
        self.admin_field2 = admin_field2

class SupportUser:
    def __init__(self, support_field1, support_field2):
        self.support_field1 = support_field1
        self.support_field2 = support_field2

class UserAdapter:
    def __init__(self, user):
        self.user = user

    def get_fields(self):
        if isinstance(self.user, AdminUser):
            return self.user.admin_field1, self.user.admin_field2
        elif isinstance(self.user, SupportUser):
            return self.user.support_field1, self.user.support_field2
        else:
            raise ValueError("Invalid user type")

# Приклад використання
admin_user = AdminUser("admin_field1_value", "admin_field2_value")
support_user = SupportUser("support_field1_value", "support_field2_value")

admin_user_adapter = UserAdapter(admin_user)
support_user_adapter = UserAdapter(support_user)

admin_field1, admin_field2 = admin_user_adapter.get_fields()
print(f"Admin User: Field1={admin_field1}, Field2={admin_field2}")

support_field1, support_field2 = support_user_adapter.get_fields()
print(f"Support User: Field1={support_field1}, Field2={support_field2}")
