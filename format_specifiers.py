"""format specifiers = {value:flags} format a value based on what flags are inserted
"""
from PIL.ImageQt import align8to32
from reportlab.rl_settings import spaceShrinkage

from dictionary import values

"""
.(number)f = round to that many decimal places (fixed point)
:(number) = allocate that many spaces
:03 = allocate and zero pad that many spaces
:< = left justify
:> = right justify
:^ = center align
:+ = use a plus sign to indicate positive values
:= = place sign to leftmost position
: = insert a space before positive numbers
:, = comma separator
"""

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:<.2f}")
print(f"Price 3 is ${price3:>.2f}")


print(f"Price 1 is ${price1:010}")
print(f"Price 1 is ${price1:<10}")

print(f"Price 1 is ${price1:^10}")

