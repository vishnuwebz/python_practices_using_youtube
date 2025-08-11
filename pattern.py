from while_ex import MAX_ATTEMPTS

for i in range(4):
    for j in range(4):
        print("# ", end = "")

    print()


for a in range(4):
    for b in range(a + 1):
        print("^", end="")
    print()

for x in range(4):
    for y in range(4 - x):
        print("*", end="")
    print()

users = ["Alice", "Bob", "Eve", "Charlie"]
blocked = ["Eve"]

for user in users:
    if user in blocked:
        continue
    print("Send message to:", user)

MAX_ATTEMPTS = 3
correct_pwd = "python123"

for attempt in range(MAX_ATTEMPTS):
    pwd = input("Enter your password: ")
    if pwd == correct_pwd:
        print("Login Successful!")
        break
else:
    print("Too many failed attempts!")