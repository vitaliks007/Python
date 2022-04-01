def max_elem(th_set):
    max_e = th_set[0]
    for elem in th_set:
        if elem > max_e:
            max_e = elem
    return max_e


def min_elem(th_set):
    min_e = th_set[0]
    for elem in th_set:
        if elem < min_e:
            min_e = elem
    return min_e
