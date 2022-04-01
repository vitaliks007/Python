import math


def main(b, a, m, z):
    f = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            f += 80 + pow(81 * pow(j, 3), 2) + 32 * pow(math.atan(i), 6)

    for j in range(1, m + 1):
        for k in range(1, a + 1):
            f += pow(math.cos(z), 4) / 26 - \
                 pow(49 * pow(j, 3) - k - 0.01, 3 / 2) / 90 - 0.01
    return f


print(main(6, 7, 3, 0.66))
