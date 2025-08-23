a = 5
b = 4

print(a < 8 and b < 5) # True

print(a < 8 and b < 2) # False

x = True
print(x)

print(not x)

print(bin(25)) # 0b11001

print(oct(25)) # 0o31

print(hex(25)) # 0x19


temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️")
elif temp <= 0 and is_sunny:
    print("it is COLD outside 🥶")
    print("It is SUNNY ☀️")
# elif temp < 28 and temp > 0 and is_sunny:
elif 28 > temp > 0 and is_sunny:
    print("it is WARM outside 😃")
    print("it is SUNNY ☀️")