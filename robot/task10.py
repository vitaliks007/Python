def main(table):
    temp = []
    for row in table:
        if (row not in temp) and not (row[0] is None):
            temp.append(row)
    table = temp

    for row in table:
        elems = row[0].split('-')
        elems = elems[::-1]
        row[0] = '.'.join(elems)

        row[1] = row[1].replace('[at]', '@')

        elems = row[2 + 1].split(':')
        row[2] = ' '.join(elems[0].split(' ')[::-1])
        row[3] = format(float(elems[1]), '.4f')

    return table


# table = [['2001-04-16', 'lumomman58[at]rambler.ru', 'lumomman58[at]rambler.ru', 'Лумомман Федор:0.5'],
#          ['2001-12-16', 'leonid44[at]yahoo.com', 'leonid44[at]yahoo.com', 'Бибев Леонид:0.1'],
#          ['1999-04-19', 'sisesov27[at]mail.ru', 'sisesov27[at]mail.ru', 'Шисешов Роман:0.3'],
#          ['2001-01-24', 'kuzofov31[at]gmail.com', 'kuzofov31[at]gmail.com', 'Кузофов Родион:0.8'],
#          ['2001-01-24', 'kuzofov31[at]gmail.com', 'kuzofov31[at]gmail.com', 'Кузофов Родион:0.8'],
#          ['2001-01-24', 'kuzofov31[at]gmail.com', 'kuzofov31[at]gmail.com', 'Кузофов Родион:0.8'],
#          [None, None, None, None]]
table = [['2001-04-16', 'lumomman58[at]rambler.ru', 'lumomman58[at]rambler.ru', 'Лумомман Федор:0.5'],
         ['2001-12-16', 'leonid44[at]yahoo.com', 'leonid44[at]yahoo.com', 'Бибев Леонид:0.1'],
         ['1999-04-19', 'sisesov27[at]mail.ru', 'sisesov27[at]mail.ru', 'Шисешов Роман:0.3'],
         ['2001-01-24', 'kuzofov31[at]gmail.com', 'kuzofov31[at]gmail.com', 'Кузофов Родион:0.8'],
         ['2001-01-24', 'kuzofov31[at]gmail.com', 'kuzofov31[at]gmail.com', 'Кузофов Родион:0.8'],
         [None, None, None, None],
         [None, None, None, None],
         ['2001-01-24', 'kuzofov31[at]gmail.com', 'kuzofov31[at]gmail.com', 'Кузофов Родион:0.8']]
print(main(table))
