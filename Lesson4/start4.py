import random

# class Person:

# #    Constructor
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         print("Constructor working...")

# # Destructor
#     def __del__(self):
#         print("Destructor working...")

#     def person_info(self):
#         print(self.__name, "is", self.__age, "years old")

#     @property
#     def name(self):
#         return self.__name

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, new_age):
#         if self.__age == new_age:
#             print("The same age")
#         else:
#             self.__age = new_age


# Екземпляр класу
# bill = Person("Bill", 56)
# print("Age before:", bill.age)
# bill.age = 57
# print("Age after:", bill.age)

# bill.person_info()

# print(bill.get_name())
# print("Before:",bill.get_age())
# bill.set_age(57)
# print("After:",bill.get_age())

# tom = Person("Tom", 39)
# tom.person_info()

# adam = Person("Adam", 29)
# eva = Person("Eva", 27)
# tina = Person("Tina", 32)
# stephany = Person("Stephany", 22)

# person_list = []

# person_list.append(bill)
# person_list.append(tom)
# person_list.append(adam)
# person_list.append(eva)
# person_list.append(tina)
# person_list.append(stephany)


# for person in person_list:
#     # person.person_info()
#     print(person.name, "=", person.age)
#     person.age += 1

# print("=====================================================")

# for person in person_list:
#     # person.person_info()
#     print(person.name, "=", person.age)


class Account:

    def __init__(self, account, money, currency):
        self.__account = account
        self.__money = money
        self.__currency = currency

    def account_info(self):
        print("Account number:", self.__account, "Amount:",
              self.__money, "Currency", self.__currency)

    @property
    def account(self):
        return self.__account

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, add_money):
        if self.__money == add_money:
            print("No changes to the account")
        else:
            self.__money += add_money

    @money.setter
    def withdraw_money(self, withdraw_money):
        if self.__money == withdraw_money:
            print("No changes to the account")
        else:
            self.__money -= withdraw_money


print("Bill M. Account:")
bill = Account(random.randint(100000, 999999), 10600, "USA")
bill.account_info()
print("Bill's account before:", bill.money)
bill.money = int(input("Enter amount to add: "))
print("Bill's account after:", bill.money)
print("=====================================================")
print("Bill's account before withdrawal:", bill.money)
bill.withdraw_money = int(input("Enter witdrawal amount: "))
print("Bill's account after withdrawal:", bill.money)
print("=====================================================")
print("Adam D. Account:")
adam = Account(random.randint(100000, 999999), 11201, "USA")
adam.account_info()
print("Adam's account before:", adam.money)
adam.money = int(input("Enter amount to add: "))
print("Adam's account after:", adam.money)
print("=====================================================")
print("Adam's account before withdrawal:", adam.money)
adam.withdraw_money = int(input("Enter witdrawal amount: "))
print("Adam's account after withdrawal:", adam.money)
print("=====================================================")
