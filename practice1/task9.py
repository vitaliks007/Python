def naive_mul(x, y):
    r = x
    for i in range(0, y - 1):
        x = x + r


naive_mul(10, 15)