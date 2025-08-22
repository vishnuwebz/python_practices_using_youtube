import math

score = 0

num = float(input("Q1: Enter a number to find square root: "))
ans = float(input(f"What is sqrt({num})? "))

if ans == math.sqrt(num):
    print("Correct!")
    score += 1
else:
    print(f"Wrong. The answer is {math.sqrt(num)}")

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")

import math

def bill_calculator(prices, tax_percent):
    # step 1: sum up prices
    total = sum(prices)
    # step 2: calculate tax
    tax = total * tax_percent / 100
    # step 3: get grand total
    grand_total = total + tax
    # step 4: round up ro next rupee for payment
    payable = math.ceil(grand_total)
    # step 5: display everything
    print("Item Prices:", prices)
    print("Subtotal:", total)
    print(f"Tax (@{tax_percent}%):", tax)
    print("Amount payable (rounded):", payable)

item_prices = [99.99, 120.45, 250.75, 67.30]
tax_rate = 18
bill_calculator(item_prices, tax_rate)