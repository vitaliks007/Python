import math


def main(n):
    if n == 0:
        return -0.47
    elif n == 1:
        return 0.69
    elif n >= 2:
        return pow(math.atan(pow(main(n-2), 3) - 4 * main(n-2)), 2) \
               - 47 * math.log(71 - pow(main(n-1), 3), 2) - 74


print(main(9))
