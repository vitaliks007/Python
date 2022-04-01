from pathlib import Path
import tkinter as tk

SCALE_X = 6
SCALE_Y = 4

COLORS = [
    (0, 0, 0),
    (0, 0, 168),
    (0, 168, 0),
    (0, 168, 168),
    (168, 0, 0),
    (168, 0, 168),
    (168, 84, 0),
    (168, 168, 168),
    (84, 84, 84),
    (84, 84, 252),
    (84, 252, 84),
    (84, 252, 252),
    (252, 84, 84),
    (252, 84, 252),
    (252, 252, 84),
    (252, 252, 252)
]


def draw_line(coords, color_index):
    if len(coords) <= 1:
        return
    canvas.create_line(*[(x * SCALE_X, y * SCALE_Y) for x, y in coords],
                       fill='#%02x%02x%02x' % COLORS[color_index], width=4)


def draw_y_corner(args, color):
    x, y = args[0], args[1]
    coords = [(x, y)]
    iftp = 0
    for arg in args[2:]:
        if iftp % 2 == 0:
            x, y = (x, arg)
        else:
            x, y = (arg, y)
        coords.append((x, y))
        iftp += 1
    draw_line(coords, color)


def draw_x_corner(args, color):
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
    draw_line(coords, color)


def draw_abs_line(args, color):
    coords = []
    for x, y in args:
        coords.append((x, y))
    draw_line(coords, color)


def draw_rel_line(args, color):
    x, y = args[0], args[1]
    coords = [(x, y)]
    for arg in args[2:]:
        x += ((arg & 112) >> 4) * pow(-1, (arg & 128) >> 7)
        y += (arg & 7) * pow(-1, (arg & 8) >> 3)
        coords.append((x, y))
    draw_line(coords, color)


def draw(pic):
    last = 0
    coms = {}
    for byte in pic:
        if byte >= 0xF0:
            last = byte
        else:
            try:
                coms[last].append(byte)
            except Exception:
                coms[last] = [byte]

    active = False
    color = COLORS[0]
    for com in coms.keys():
        args = coms[com]
        match com:
            case 0xF0:
                active = True
                color = args[0]
            case 0xF1:
                active = False
            case 0xF4:
                if active:
                    draw_y_corner(args, color)
            case 0xF5:
                if active:
                    draw_x_corner(args, color)
            case 0xF6:
                if active:
                    draw_abs_line(args, color)
            case 0xF7:
                if active:
                    draw_rel_line(args, color)


pic = Path('data/PIC.1').read_bytes()
canvas = tk.Canvas(width=160 * SCALE_X, height=170 * SCALE_Y)
canvas.pack()
draw(pic)
tk.mainloop()
