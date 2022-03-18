def max_elem(th_set):
    max_e = th_set[0]
    for elem in th_set:
        if elem > max_e:
            max_e = elem
    return max_e


def print_set(th_set):
    for elem in th_set:
        print(elem)


def min_elem(th_set):
    min_e = th_set[0]
    for elem in th_set:
        if elem < min_e:
            min_e = elem
    return min_e


def zero_fill(th_set):
    for elem in th_set:
        elem = 0
