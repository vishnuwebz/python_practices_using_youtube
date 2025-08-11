"""
for i in range(rows):
    # print spaces or characters
    for j in range(columns):
        print("*", end=" ")
    print() # move to next line
"""

# pattern 1: right-angled triangle

rows = 5
for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""

print("############################################")

# pattern 2: inverted triangle

rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
* * * * * 
* * * * 
* * * 
* * 
*
"""

print("############################################")

# pattern 3: pyramid pattern

rows = 5
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("* " * (i + 1))

"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""

print("############################################")

# number pyramid

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
# diamond shaped stars

n = 5
# upper half
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))
# lower half
for i in range(n-2, -1, -1):
    print(" " * (n - i - 1) + "* " * (i + 1))

