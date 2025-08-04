# ex 1

import math 

length = 4
width = 3
diagonal = math.sqrt(length**2 + width**2) # sqrt(a² + b²)
print(f"Diagonal length: {diagonal}")

# Diagonal length: 5.0

# ex 2

# round prices in billing system 

import math 

price = 15.75
print("Rounded price:", math.floor(price))

print("Rounded up price:", math.ceil(price))

# Rounded price: 15
# Rounded up price: 16

# ex 3

# calculate compound interest with power function

principal = 10000
rate = 0.05
time = 5

amount = principal * math.pow((1 + rate), time)
print(f"Compound interest amount: {amount}")
# Compound interest amount: 12766.28


# mp 1

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / math.pow(height, 2)
print(f"BMI: {bmi:.2f}")

# Enter height in meters: 1.75
# Enter weight in kg: 75
# BMI: 25.22

# major project: Scientific Project

# supports square roots, power, floor, ceil
# uses loops, functions, user input validation
# combines previous topics( functions, operator, input handling, conditionals)

import math

def sci_calc():
    while True:
        print("\n1. Square Root")
        print("2. Power")
        print("3. Floor")
        print("4: Ceil")
        print("5. Exit")

        choice = input("Choose operation: ")

        if choice == "1":
            num = float(input("Enter number: "))
            print("Square root:", math.sqrt(num))
        elif choice == "2":
            base = float(input("Enter base: "))
            exp = float(input("Enter exponent: "))
            print("Result:", math.pow(base, exp))
        elif choice == "3":
            num = float(input("Enter number: "))
            print("Floor value:", math.floor(num))
        elif choice == "4":
            num = float(input("Enter number: "))
            print("Ceil value:", math.ceil(num))
        elif choice == '5':
            print("Exiting Calculator")
            break
        else:
            print("Invalid Input")
sci_calc()
