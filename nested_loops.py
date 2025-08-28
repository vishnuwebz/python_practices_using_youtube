"""
nested loops - A loop within loop (outer, inner)
    outer loop:
        inner loop:
"""

for x in range(1, 10):
    # print(x, end="\n") # by default it ends with \n: new line character
    print(x, end="")
print()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

for a in range(3):
    for b in range(1, 10):
        print(b, end="")
    print()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

rows = int(input("Enter the number of rows: ")) # outer-loop
columns = int(input("Enter the number of columns: ")) # inner-loop
symbols = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbols, end="")
    print()

print("***************************************************")
# nested loops extra

# multiplication table for 1 to 5

for i in range(1, 6): # outer loop for numbers 1 to 5
    for j in range(1, 11): # inner loop for multiplying by 1 to 10
        print(f"{i} x {j} = {i * j}", end="\t")
    print() # new line after each row


print("***************************************************")

# printing a grid of stars 3 rows x 5 columns

for o in range(3):
    for p in range(5):
        print("*", end="")
    print()
print("***************************************************")

# list all possible pairs of students

students = ["Alice", "Bob", "Charlie"]

for s1 in students:
    for s2 in students:
        if s1 != s2:
            print(f"Pair: ({s1}, {s2})")

# pair each student with every other student without pairing with self.

print("***************************************************")

# print elements of a 2D matrix

matrix = [[1,2,3], [4,5,6]]

for row in matrix:
    for value in row:
        print(value, end="")
    print() # new line after each row

print("***************************************************")

s1 = "abc"
s2 = "bcd"

for ch1 in s1:
    for ch2 in s2:
        if ch1 == ch2:
            print(ch1)

# for each charater in s1, compare with each in s2, print if matching

print("***************************************************")

# mini projects

# generate labels for seats in a theatre or classroom

rows = 3   # Number of rows
cols = 4   # Number of seats per row

for row in range(1, rows + 1):         # For each row
    for col in range(1, cols + 1):     # For each seat in row
        seat_label = f"{chr(64 + row)}{col}"  # Converts row number to letter (1->A, 2->B)
        print(seat_label, end=" ")
    print()                            # New line after each row

# outer loop iterates over rows