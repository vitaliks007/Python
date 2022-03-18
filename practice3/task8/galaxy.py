from PIL import Image, ImageFont, ImageDraw

def tweakseed(s):
    temp = sum(s) % 0x10000
    s[0] = s[1]
    s[1] = s[2]
    s[2] = temp

    return s


def makesystem(s, pairs):
    name = [' ' for k in range(0, 8)]
    longnameflag = s[0] & 64
    x = s[1] >> 8
    y = s[0] >> 8

    pair1 = 2 * ((s[2] >> 8) & 31)
    s = tweakseed(s)
    pair2 = 2 * ((s[2] >> 8) & 31)
    s = tweakseed(s)
    pair3 = 2 * ((s[2] >> 8) & 31)
    s = tweakseed(s)
    pair4 = 2 * ((s[2] >> 8) & 31)
    s = tweakseed(s)

    name[0] = pairs[pair1]
    name[1] = pairs[pair1 + 1]
    name[2] = pairs[pair2]
    name[3] = pairs[pair2 + 1]
    name[4] = pairs[pair3]
    name[5] = pairs[pair3 + 1]

    if longnameflag:
        name[6] = pairs[pair4]
        name[7] = pairs[pair4 + 1]

    name = ". " + "".join([elem for elem in name if elem != '.'])

    return x, y, name, s


pairs_n = '..LEXEGEZACEBISO' 'USESARMAINDIREA.' 'ERATENBERALAVETI' 'EDORQUANTEISRION'
seed = [0x5A4A, 0x0248, 0xB753]
systems = []
galaxy = ''
for i in range(0, 256):
    x, y, s_name, seed = makesystem(seed, pairs_n)
    systems.append({'x': x, 'y': y, 'name': s_name})

for i in range(0, 2560, 10):
    for j in range(0, 2560, 10):
        system = [system for system in systems if system['y'] == i / 10 and system['x'] == j / 10]
        if len(system) == 0:
            galaxy += ' ' * 8
        else:
            galaxy += system[0]['name']
    galaxy += '\n'


img = Image.new('RGB', (8800, 4800), color=(0, 0, 0))
font = ImageFont.truetype("arial.ttf", 15)
ImageDraw.Draw(img).text((0, 0), galaxy, font=font, fill=(255, 255, 255))
img.save("galaxy.png")
