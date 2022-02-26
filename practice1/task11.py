def fast_mul_gen(x, z):
    s = ""
    res = 0
    y = 1
    temp = x

    while temp > 1:
        res += z * (temp % 2)
        temp = temp // 2
        y *= 2
        s += "x = x + x\n"
        z *= 2
    res += z * (temp % 2)

    if x != y:
        s = "y = x\n" + s + "x = x"
    for i in range(y, x):
        s += " + y"

    print(res)
    return s


x, y = map(int, input().split())
print(fast_mul_gen(y, x))