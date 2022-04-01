args = [4, 7, 6, 3, 5]
x, y = args[0], args[1]
coords = [(x, y)]
iftp = 0
for arg in args[2:]:
    if iftp % 2 == 1:
        x, y = (x, arg)
    else:
        x, y = (arg, y)
    coords.append((x, y))
    iftp += 1


for x, y in coords:
    print(x, y)