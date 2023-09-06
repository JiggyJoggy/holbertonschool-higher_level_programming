#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = str(number)
print(f"Last digit of {number} is {int(last_num[-1])}")
