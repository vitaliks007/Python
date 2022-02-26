import math


def main(z, x):
    y = math.sqrt(math.pow(math.asin(z), 3) + math.pow(1 - z - math.pow(x, 3), 4) / 47) \
        + math.sqrt(math.pow(z, 6) + 17 * math.pow(math.cos(x), 5))
    return y


print(main(0.3, -0.05))
