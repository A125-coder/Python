# env.mod (enviroment)
from lib.calc import summ, minus, division, mult


# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))

# def sum(a, b):
#     print(a + b)
#     input('Press any key to continue')

# sum(a, b)

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
# params = input('Enter number: ')

choice = input(
    "Enter your choice: \n1.Add\n2.Subtract\n3.Divide\n4.Multiply\n5.Exit => ")

if choice == 1:
    print("Summ: ", summ(a, b))
elif choice == 2:
    print("Subtract: ", minus(a, b))
elif choice == 3:
    print("Division: ", division(a, b))
elif choice == 4:
    print("Multiply: ", mult(a, b))