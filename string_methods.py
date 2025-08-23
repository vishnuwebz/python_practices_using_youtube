# string methods

# name = input("Enter your full name: ")

# result = len(name)
# result = name.find("o")
# result = name.rfind("q")
# print(result)
# name = name.capitalize()

# name = name.upper()
# name = name.lower()
# print(name)


# result = name.isdigit()
# print(result)

# result = name.isalpha()
# print(result)

# phone_number = input("Enter your phone #: ")

# result = phone_number.count('-')
# print(result)
"""Enter your phone #: 90-74-64-04-25
4"""

# result = phone_number.replace("-", " ")

# print(result)

"""
Enter your phone #: 90-74-64-04-25
90 74 64 04 25
"""

"""validate user input exercise
1: username is no more than 12 characters
2: username must not contain spaces
3: username must not contain digits
"""

username = input("Enter a username: ")
username.find(" ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1: # if there is space
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
