"""for loops = execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc..."""

# for x in range(1, 11):
#     print(x)

# for counter in reversed(range(1, 11, 1)):
#     print(counter)
# print("HAPPY NEW YEAR!")
#
#
# credit_card = "1234-5678-9012-3456"
#
# for x in credit_card:
#     print(x)


for i in range(1, 21):
    if i == 13:
        break
    else:
        print(i)


# countdown timer

import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    # print(f"00:00:{seconds:02}") # we had implemented format specifiers 2 digits 0 digit paddings
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
# time.sleep(3)

print("TIME'S UP!")