# https://projecteuler.net/problem=2

x = 1
y = 2
sum = 0

while min(x, y) < 4000000:
    if min(x, y) % 2 == 0:
        sum += min(x, y)
        if x < y:
            x += y
        else:
            y += x
    else:
        if x < y:
            x += y
        else:
            y += x

print(sum)

# 4613732
