age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
else:
    print("You must be 18+ to sign up!")

print("////////////////////////////////////////////")

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

print("////////////////////////////////////////////")

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")