# https://projecteuler.net/problem=4

palindrome = 0

for x in range(100, 999):
    for y in range(100, 999):
        z = str(x * y)
        n = x * y
        if z == z[::-1]:
            if n > palindrome:
                palindrome = n

print(palindrome)

# 906609
