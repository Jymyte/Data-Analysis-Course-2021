import random

def ripuli(y):
    for i in range(10):
        x = random.random()
        x += y
        print(x)

ripuli(1)