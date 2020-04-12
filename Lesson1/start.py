import random
# print("Hello World!")

# a = 10  # int
# print(a, type(a))

# a = 10.6  # float
# print(a, type(a))

# a = True  # boolean
# print(a, type(a))

# a = "Bill"  # str
# print(a, type(a))


# name = input("Your name: ")
# age = int(input("Your age: "))
# print(name, type(name))
# print(age, type(age))


# a = int(input("Number1: "))
# b = int(input("Number2: "))
# c = int(input("Number3: "))

# sum = a+b
# min = a-b
# mult = a*b
# dev = a/b
# print("Sum = ", sum)
# print("Min = ", min)
# print("Mult = ", mult)
# print("Dev = ", dev)


# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a = b")

# if a > b and a > c:
#     print("first if ")
# elif a > b or b > c:
#     print("elif")


# rnd = random.randrange(-20, 10)
# print(rnd)


# Задача 1
# Напишіть програму, яка переводить кілометри в метри. Кілометри вводяться з клавіатури.

# km = int(input("Enter kilometrs: "))

# metr = km/1000

# print("Result = ", metr)


# Задача 2
# Разрабити програму, яка організовує діалог з користувачем і дозволяє обчислити по вказаній сумі і курсу євро, долара та російськогл рябля суму в гривнях.

# Eur_curs = 29.8
# Dol_curs = 27.4
# Rub_curs = 0.35
# uah = int(input("Enter val: "))


# Eur = uah/Eur_curs
# Dol = uah/Dol_curs
# Rub = uah/Rub_curs

# print("EU = ", Eur)
# print("US = ", Dol)
# print("Rub = ", Rub)

# Задача 3
# Дано витрати машиною пального на 100 км, ціну 1 л пального, а також шлях, який потрібно проїхати водію. Обчислити та вивести на екран скільки потрібно витратити грошей водію, щоб проїхати вказаний шлях

# a = int(input('Vutrata 1l/100km: '))
# b = int(input('Price 1l: '))
# c = int(input('Distance: '))

# res = print('Point', c / a * b)

# Задача 4
# Дано три числа. Визначити чи рівні вони між собою.

# a = random.randrange(20, 40)
# b = random.randrange(10, 50)
# c = random.randrange(10, 40)
# print(a, b, c)

# if a == b and b == c and a == c:
#     print("Equal")


# exit = False

# while not exit:
#     choice = int(input("1. Add\n2. Div\n0. Exit\n==>"))
#     if choice == 1:
#         print("a + b")
#     elif choice == 2:
#         print("a / b")
#     elif choice == 0:
#         exit = True


# exit = False

# while not exit:
#     a = (input("Enter number 1: "))
#     b = (input("Enter number 2: "))
#     choice = int(input("1. Add\n2. Min\n3. Mult\n4. Div\n0. Exit\n==>"))
#     if choice == 1:
#         print("a + b")
#     elif choice == 2:
#         print("a - b")
#     elif choice == 3:
#         print("a * b")
#     elif choice == 4:
#         print("a / b")
#     elif choice == 0:
#         exit = True


# Протягом тижня вимірювали температуру повітря. Знайти кількість днів, коли температура перевищувала 10o С

# i = 0
# counter = 0

# while i < 7:
#     i += 1
#     t = random.randint(-10, 30)
#     if t > 10:
#         counter += 1
#     print(t)

#     print("More then 10 ==> ", counter)


# num = 8
# counter = 0

# for i in range(1, num):
#     t = random.randint(-10, 30)
#     if t > 10:
#         counter += 1
#         print(t)


# print("More then 10 ==> ", counter)


