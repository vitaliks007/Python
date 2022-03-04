from random import randint

alph = "ЦУКЕНГШЗХФВАПРОЛДЖЭЯЧСМИТБЮ"
root = ['Красн', 'Гиацин', 'Орл', 'Захар', 'Герасим', 'Зерн', 'Кедр', 'Щедр', 'Ведр', 'Кир']
suf = ['ов', 'ин', 'овых', 'ова']
name = ['Александр', 'Петр', 'Иван', 'Артем', 'Артур', 'Вадим', 'Влад', 'Всеволод', 'Ярослав', 'Давид',
        'Ева', 'Наталья', 'Герда', 'Нина', 'Анастасия', 'Елена', 'Хина', 'Оксана', 'Надежда', 'Елизавета']
end = ['ович', 'овна']

n = int(input())
for i in range(n):
        gend = randint(0, 1)
        curName = name[randint(0, 9) + gend * 10]
        curPatron = name[randint(0, 9)] + end[gend]
        curSubname = root[randint(0, 9)] + suf[randint(0, 2) if gend == 0 else randint(2, 3)]
        print(curName + ' ' + curPatron + ' ' + curSubname)
