# ex 1 rectangle area calc

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is : {area}cm squared")

print("###########################################")

# ex2: shopping cart program

# item, price, quantity

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity =  int(input("How many would you like?: "))
total = price * quantity

print(f"The total price for {quantity} {item}'s is: {total}rs.")

print("###########################################")

# Madlibs game
# word game where you create ad story by filling in blanks with random words

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending wih 'ing': ")
adjective3 = input("Enter an adjective (description): ")
print("***************************************************")
print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")
