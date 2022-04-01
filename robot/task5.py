import math


def main(z, x):
    n = len(x)
    sum = 0
    x.append(x[n - 1])
    z.append(z[n - 1])
    for i in range(n - 1, 0, -1):
        x[i] = x[i - 1]
        z[i] = z[i - 1]
    for i in range(1, n + 1):
        sum += 30 * pow(59 * x[n + 1 - math.ceil(i / 2)]
                        - pow(z[math.ceil(i / 3)], 3) - 0.04, 6)
    return sum


print(main([0.67, 0.96, 0.12],
           [-0.73, -0.28, 0.81]))
