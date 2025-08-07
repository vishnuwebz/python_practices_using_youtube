# input validation

password = ""
while password != "python123":
    password = input("Enter password: ")
    print("Try again!")
print("Access granted")

# sum all numbers until zero

total = 0
n = int(input("Enter a number (0 to stop): "))
while n != 0:
    total += n
    n = int(input("Enter a number (0 to stop): "))
print("Sum:", total)

# Countdown Timer

count = 5

while count > 0:
    print("T-minus", count)
    count -= 1
print("Blast off!")

# simple login system

MAX_ATTEMPTS = 3
attempts = 0
correct_password = "admin@123"

while attempts < MAX_ATTEMPTS:
    pwd = input("Enter password")
    if pwd == correct_password:
        print("Login successful")
        break
    else:
        print("Try again")
        attempts += 1

else:
    print("Access locked. Too many attempts.")

#ATM Withdrawal Simulation

balance = 5000

while True:
    amount = int(input("Enter withdrawal amount (0 to exit): "))
    if amount == 0:
        break
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print("Withdrawal successful. Balance:", balance)
print("Session ended.")


