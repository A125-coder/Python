import random
# 1. Написати програму яка в залежності від введеної години виводить: good night, good day, good evening, good morning.

# hour = float(input("Enter hours 0 - 24: "))

# if 6 < hour <= 12:
#     print('Good morning')
# elif 12 < hour <= 17:
#     print('Good day')
# elif 17 < hour <= 22:
#     print('Good evening')
# else:
#     print('Good night')

# 2. Відомо, що 1 дюйм дорівнює 2.54 см. Розробити програму, що переводить дюйми в сантиметри и навпаки. Діалог с користувачем реалізувати через систему меню.

# d_cm = 2.54

# exit = False

# while not exit:
#     choice = int(input("1. Inch\n2. Cm\n0. Exit\n "))
#     if choice == 1:
#         cm = float(input("Enter cm: "))
#         print('Inches => ', cm * d_cm)
#     elif choice == 2:
#         inch = float(input("Enter inch: "))
#         print('Cm => ', inch / d_cm)
#     elif choice == 0:
#         exit = True


# 3. Розробити програму, що переводить значення температури в градусах по Цельсію в температуру по Фаренгейту та навпаки. Співвідношення між температурами визначається формулою: TF = TC *1.8 +32. Діалог с користувачем реалізувати через систему меню.


# exit = False

# while not exit:
#     choice = int(input("1. TF\n2. TC\n0. Exit\n "))
#     if choice == 1:
#         TC = float(input("Enter Celsius: "))
#         print("Fahrenheit => ", TC * 1.8 + 32)
#     elif choice == 2:
#         TF = float(input("Enter Fahrenheit: "))
#         print("Celsius => ",  (TF - 32) / 1.8)
#     elif choice == 0:
#         exit = True


# 4. Вводяться 8 чисел. Знайти добуток та середнє арифметичне цих чисел.

# mult = 1
# arithm = 0

# for i in range(8):
#     num = random.randint(0, 20)
#     print(num)
#     mult *= num
#     arithm += num / 8

# print("Multiplying: ", mult)
# print("Arithmetic mean: ", arithm)


# 5. Протягом тижня вимірювали температуру повітря. Знайти максимальну та мінмальну температуру.

# for i in range(7):
#     t = random.randint(-20, 40)
#     print(t)
#     if i == 0:
#         min_t = max_t = t
#     else:
#         if t < min_t:
#             min_t = t
#         if t > max_t:
#             max_t = t
# print('Min: ', min_t)
# print('Max: ', max_t)
