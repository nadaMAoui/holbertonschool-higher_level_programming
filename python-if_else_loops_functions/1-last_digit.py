#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = repr(number)
last_digit_str = number_str[-1]
last = int(last_digit_str)
if number < 0:
    last = -last
print("Last digit of {:d} is {:d} and is".format(number, last), end= ' ')
if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
else:
    print("less than 6 and not 0")
