def main(x):
    a = x & 0xffff
    b = x & 0x7f0000
    c = x & 0x3f800000
    d = x & 0x40000000
    e = x & 0x80000000
    return (c << 2) + (a << 9) + (d >> 22) + (e >> 24) + (b >> 16)


print(hex(main(0x18cf028f)))
