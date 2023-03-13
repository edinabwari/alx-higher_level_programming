#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[-1] == 0:
print(f"Last digit of {number} is {number[-1]}")
