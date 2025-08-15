# https://youtu.be/38svC3U7hVo?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3

nums = [12, 13, 16 ,18, 20, 26]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
    else:
        print("not found")

num = 7

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
    else:
        print("Prime")

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

# Array in python

from array import *

vals = array('i', [5,9,8,4,2])
print(vals, "# vals")
print(vals.buffer_info(), "# buffer_info")
print(vals[2], "# vals[2]")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
for i in range(5):
    print(vals[i], "# vals[i]")


newArr = array(vals.typecode, (a for a in vals))
print(newArr)
i = 0

while i < len(newArr):
    print(newArr[i])
    i += 1

vals_2 = array('u', ['a', 'e', 'i'])
print(vals_2)

