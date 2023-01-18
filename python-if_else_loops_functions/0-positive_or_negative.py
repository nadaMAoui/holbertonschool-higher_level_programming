#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number, end=' ')
if number == 0:
    print('is zero')
if number > 0:
    print('is postive')
else:
    print('is negative')
