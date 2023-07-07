'''
2.2 Змоделювати систему оподатуквання району
В рацоні існує 5 компаній 3 видів: велика ,середня і мала компанія.
1 велика 2 середні 2 малі
Велика компанія має сплатити 10% з працівника
Середня 20 % з працівника
Мала 30 % з працівника
'''

class Company:
    def pay_tax(self, employees):
        pass


class LargeCompany(Company):
    def pay_tax(self, employees):
        tax_rate = 0.1
        return employees * tax_rate


class MediumCompany(Company):
    def pay_tax(self, employees):
        tax_rate = 0.2
        return employees * tax_rate


class SmallCompany(Company):
    def pay_tax(self, employees):
        tax_rate = 0.3
        return employees * tax_rate


class CompanyGroup(Company):
    def __init__(self):
        self.companies = []

    def add_company(self, company):
        self.companies.append(company)

    def pay_tax(self, employees):
        total_tax = 0
        for company in self.companies:
            total_tax += company.pay_tax(employees)
        return total_tax

group = CompanyGroup()

large_companies = int(input("Введіть кількість великих компаній: "))
for _ in range(large_companies):
    group.add_company(LargeCompany())

medium_companies = int(input("Введіть кількість середніх компаній: "))
for _ in range(medium_companies):
    group.add_company(MediumCompany())

small_companies = int(input("Введіть кількість малих компаній: "))
for _ in range(small_companies):
    group.add_company(SmallCompany())

employees = int(input("Введіть кількість працівників: "))
total_tax = group.pay_tax(employees)

print("Загальна сума податків: ", total_tax)
