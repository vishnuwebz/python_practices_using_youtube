import math

x = 9.1

print(math.pi)
print(math.e)
# result = math.sqrt(x)
result = math.ceil(x)
print(result)

print("////////////////////////////////////////////")

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference is: {circumference}")
print(f"the circumference is: {round(circumference, 2)}")

print(f"The area of the circle is: {area}cm^2")
print(f"The area of the circle is: {round(area, 2)}")

print("////////////////////////////////////////////")


