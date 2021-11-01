import random


def explore_only() -> int:
    h1 = 0
    h2 = 0
    h3 = 0
    i = 0
    while i < 100:
        h1 += random.normalvariate(9, 3)
        i += 1
    while i < 200:
        h2 += random.normalvariate(7, 5)
        i += 1
    while i < 300:
        h3 += random.normalvariate(11, 7)
        i += 1
    return int(h1 + h2 + h3)
