#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    lastdigit = number % 10
    lastdigit *= -1
    number *= -1
else:
    lastdigit = (number) % 10
if lastdigit == 0:
    print("Last digit of " + str(number) + " is " + str(lastdigit) +
     " and is 0")
elif lastdigit > 5:
    print("Last digit of " + str(number) + " is " + str(lastdigit) +
     " and is greater than 5")
else:
    print("Last digit of " + str(number) + " is " + str(lastdigit) +
     " and is less than 6 and not 0")
