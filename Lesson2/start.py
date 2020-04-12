import random
import copy

# Functions

# def sum():
#     print("function sum")


# sum()

# def sum(a, b):
#     print(a + b)


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# sum(a, b)


# global glob
# def sum(a=0, b=0):
#     glob = "Global vars"
#     if a > 0:
#         return a + b
#     else:
#         print("Test")
#         return 0


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# # res = sum(a, b)
# res = sum(a, b)
# print("Result = ", res)
# print(glob)

# def sum(*params):
#     res = 0
#     for item in params:
#         print(item)
#         res += item
#     return res


# result = sum(2, 5, 8, 1, 9, 4)
# print("Result => ", result)

# tmp = 10

# for i in range(1, tmp):
#     print(i)

# a = int(input("First number: "))
# b = int(input("Second number: "))


# def find_range(a, b):
#     res = 0
#     for i in range(a+1, b):
#         print("i = ", i)
#         res += i
#     return res


# 1. Написати функцію, яка отримує в якості параметрів два цілих числа і повертає суму чисел з діапазону між ними.


# a = int(input("First number: "))
# b = int(input("Second number: "))


# def find_range(a, b):
#     res = 0
#     for i in range(a+1, b):
#         print("i = ", i)
#         res += i
#     return res


# result = find_range(a, b)
# print("Result => ", result)


# 2. Написати функцію, яка отримує відстань, яку пробіг спортсмен та час пробігу і повертає швидкість спортсмена. Відстань та час пробігу вводяться користувачем


# def v(l, time):
#     return l/time


# l = float(input("Enter length: "))
# time = float(input("Enter time: "))

# res = v(l, time)
# print("Speed is", res)


# Lists

# arr = [4, 6, 7, 8, 9, 0, 5, 2, 4, 8, 8]
# # print(arr, "type => ", type(arr))
# # for i in arr:
# #     print(i)
# print("=====================================================")

# arr[2] = 100
# for i in arr:
#     print(i)


# arr.append(99)
# print("=====================================================")

# arr[2] = 100
# for i in arr:
#     print(i)
# print("=====================================================")
# arr.insert(2, 150)
# for i in arr:
#     print(i)


# arr.remove(4)
# print("=====================================================")
# for i in arr:
#     print(i)


# print("index: ", arr.index(0))


# print("ARR Length: ", len(arr))
# print("Count: ", arr.count(8))


# arr.pop()

# print("After pop: ")
# for i in arr:
#     print(i)

# print("Sort =====================================================")
# arr.sort()
# for i in arr:
#     print(i)


# print("Reverse =====================================================")
# arr.reverse()
# for i in arr:
#     print(i)


# print("Max => ", max(arr))
# print("Min => ", min(arr))


# arr = [4, 6, 7, 8, 9, 0, [55, 43, 34], 2, 4, 8, 8, "Works", True]
# print(arr)
# arr[6][1] = 90
# print(arr)


# person = ["Tom", "Phill", "Bill", "Adam"]
# for i in person:
#     print(i)

# person.sort()
# for i in person:
#     print(i)


# 3. Дано список 10 елементів . Замінити всі від’ємні елементи додатніми.  Діапазон - 20 +30

# a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(len(a)):
#     a[i] = random.randint(-20, 30)
# print(a)
# for i in range(len(a)):
#     if a[i] < 0:
#         a[i] = -a[i]
# print(a)


# lang = ["C++", "Python", "JS", "C#", "Java", "PHP", "CSS", "HTML"]

# prog = lang
# print(prog)
# prog[0] = "Kotlin"
# print("prog => ", prog)
# print("lang => ", lang)


# prog = copy.deepcopy(lang)
# prog[0] = "Kotlin"
# print("prog => ", prog)
# print("lang => ", lang)


# part = lang[:2]
# print(part)

# part = lang[2:8:3]
# part = lang[:5]
# print(part)


# car = ("BMV", "Renault", "VW", "Audi")
# print(car)

# for i in car:
#     print(i)

# print(car[-1])

# print(len(car))
# print("Audi:", car.count("Audi"))

# i = 0
# while i < len(car):
#     print(car[i])
#     i+=1

# person = ("Bill", 34)

# name, age = person

# print("Name: ", name, "\nAge: ", age)




# Dictionary

countries = {
    "UA":"Ukraine",
    "US":"USA",
    "GB":"Great Britain",
}

for key, value in countries.items():
    print(key, "=====", value)


countries.pop("US")
print("========After==========")


for key, value in countries.items():
    print(key, "=====", value)

# for key in countries.keys():
#     print(key)

# for value in countries.values():
#     print(value)

# print(countries["GB"])

# print(countries.get("GB"))

countries["IT"] = "Italy"
print("========After==========")


for key, value in countries.items():
    print(key, "=====", value)
