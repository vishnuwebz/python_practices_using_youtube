from array import *

arr = array('i', [])

n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search: "))

k = 0
for e in arr:
    if e == val:
        k += 1
        print(k)
        break

print(arr.index(val))
