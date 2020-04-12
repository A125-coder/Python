# env.mod (enviroment)
from lib.calc import summ, minus, division, mult


# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))

# def sum(a, b):
#     print(a + b)
#     input('Press any key to continue')

# sum(a, b)


choice = input(
    "Enter your choice: \n1.Add\n2.Subtract\n3.Divide\n4.Multiply\n5.Exit => ")

param = input("Enter numbers: ").split()
params = [int(i) for i in param]

if choice == '1':
    print("Summ: ", summ(params))
elif choice == '2':
    print("Subtract: ", minus(params))
elif choice == '3':
    print("Division: ", division(params))
elif choice == '4':
    print("Multiply: ", mult(params))
else:
    print('Invalid input value')
