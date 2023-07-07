'''
2.4
Створити класи конверторів TxtConvertor PdfConvertor AviConvertor
Кожен з них має дію convert(конвертувати) яка має приймати параметр data
Результатом має бути напис для TxtConvertor ‘Преетворнено до txt’
І відповідно для інших конвертаторів
Далі користувач вводить дані в змінну data програма запропонує обрати
конвертор далі в залежності від вибору обраний об’єкт виконає дію convert
Вивести результат виконання
'''

class TxtConverter:
    def convert(self,data):
        return f"Дані-{data} переведени в TXT формат"

class AVIConverter:
    def convert(self,data):
        return f"Дані-{data} переведени в AVI формат"

class PdfConverter:
    def convert(self,data):
        return f"Дані-{data} переведени в PDF формат"
    
class Converter:
    available_converters = {'txt': TxtConverter(),
                            'avi': AVIConverter(),
                            'pdf': PdfConverter()}
    def convert(self,data,data_format):
        converter = self.available_converters.get(data_format)
        return converter.convert(data)


converter = Converter()
user_data = input("Введіть дані:")
choice = input("1 в txt 2 в avi 3 в pdf: ")

choices = {"1": "txt",
           "2": "avi",
           "3": "pdf"}

if choice in choices:
    data_format = choices.get(choice)
    print(converter.convert(user_data,data_format))