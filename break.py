av = 10

x = int(input("How many candies you want?: "))

i = 1

while i <= x:

    if i > av:
        print("Out of stock!")
        break
    print("Candy")
    i += 1

print("Bye")


for i in range(1, 50):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i)

print("Bye")


for i in range(1, 100):
    if(i % 2 != 0):
        pass
    else:
        print(i)
print("Bye")


