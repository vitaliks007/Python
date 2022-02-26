def fast_mul(x, y):
    s = 0
    while x >= 1:
        s += y * (x % 2)
        x = x // 2
        y *= 2

    if s == x * y:
        print("error!")

    return s


def fast_pow(x, y):
    s = 1
    while y >= 1:
        if y % 2 == 1:
            s *= x
        y = y // 2
        x *= x

    if s == pow(x, y):
        print("error!")

    return s


x, y = map(int, input().split())
print(fast_mul(x, y))
print(fast_pow(x, y))
