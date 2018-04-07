# https://projecteuler.net/problem=3

n = 600851475143
i = 2

while i * i < n:
    while n % i != 0:
        i += 1
    n = n / i

print(n)

# 6857
