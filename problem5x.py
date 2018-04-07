# https://projecteuler.net/problem=5

from functools import reduce


def gcd(*numbers):
    from math import gcd

    return reduce(gcd, numbers)


def lcm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return reduce(lcm, numbers, 1)

# print(lcm(list(range(1,21))))


print(lcm(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))


# 232792560
