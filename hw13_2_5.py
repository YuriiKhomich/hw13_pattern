'''
2.5 Створити Класс Товар (поля за Власним бажанням)
Адміністратор може створювати товари
Користувач може додати в кошик товари зазначаючи скільлки він їх придбав
'''

class Item:
    def __init__(self,
                 name,
                 price):
        self.name = name
        self.price = price


class AdminItemAdapter:
    def __init__(self,
                 item,
                 store_id,
                 place_id):
        self.item = item
        self.store_id = store_id
        self.place_id = place_id


class ClientItemAdapter:
    def __init__(self,
                 item,
                 price,
                 count):
        self.item = item
        self.price = price
        self.count = count
    
    def show(self):
        print(f"Назва - {self.item.name} кількість товару - "
              f"{self.count} стоимость - {self.price * self.count}грн.")


class Client:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        count = int(input(f"Кількість товарів для {item.name}: "))
        self.items.append(ClientItemAdapter(item, item.price, count))
    
    def show_items(self):
        total_price = 0
        for item in self.items:
            item.show()
            total_price += item.price * item.count
        print(f"Ітогова ціна: {total_price}")


item = Item("Товар1", 700)
item2 = Item("Товар2", 800)
item3 = Item("Товар3", 1800)
customer = Client()
customer.add_item(item)
customer.add_item(item2)
customer.add_item(item3)
customer.show_items()