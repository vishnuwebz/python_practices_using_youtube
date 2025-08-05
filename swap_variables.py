a = 5
b = 6

# a = b
# b = a

print(f"a: {a}")
print(f"b: {b}")

temp = a
a = b
b = temp

print(f"a: {a}")
print(f"b: {b}")

# swaping variables without a third variable

a = a + b # 11
b = a - b # 5
a = a - b # 6

print(a)
print(b)

# other method

a, b = b, a

print(a)
print(b)
