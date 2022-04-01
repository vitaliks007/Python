import re


def main(s):
    s = s.replace('\n', ' ')
    s = re.findall('((?<=local ).*?(?=;))', s)
    s = [st.split(' is ') for st in s]
    s = {st[0]: st[1] for st in s}
    return s


print(main('<sect> <block>local tion is usaesxe_290; </block>;<block>\
 local\ninoner_998 is dimaus;</block>; <block> local xege is ange_119;\n</block>; </sect>'))
