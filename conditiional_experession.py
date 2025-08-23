"""
conditional expression = a one-line shortcut for the if-else statement (ternary operator) Print or assign one of two values based on a condition x if else y
"""

num = 5
a = 6
b = 7
age = 13
temperature = 30
user_role = "admin"

# max_num = a if a > b else b
# min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(status)