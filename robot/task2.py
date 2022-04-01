def main(x):
    if x < 26:
        f = x*x - pow(86 * x, 6) - pow(x + 53 * x*x + x*x*x, 4)
    elif 26 <= x <= 112:
        f = 89 * pow(x, 3/2)
    elif 112 <= x <= 189:
        f = x / 24
    elif 189 <= x < 276:
        f = 52 - 52 * pow(67 * x + 1 + 81 * pow(x, 3), 6)
    elif x >= 276:
        f = 76 - 22 * pow(x, 7) - 47 * pow(abs(x), 6)
    return f
