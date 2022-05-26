def main(table):
    for row in table:
        for i in range(3):
            match i:
                case 0:
                    elems = row[i].split('-')
                    elems = elems.reverse
                    row[i] = '.'.join(elems)
                    break
                case 1:
                    row[i] = row[i].replace('[at]', '@')
                    break
                case 2:

    return table
