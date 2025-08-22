import math

score = 0

num = float(input("Q1: Enter a number to find square root: "))
ans = float(input(f"What is sqrt({num})? "))

if ans == math.sqrt(num):
    print("Correct!")
    score += 1
else:
    print(f"Wrong. The answer is {math.sqrt(num)}")