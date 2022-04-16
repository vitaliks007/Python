# Документация

Пример выполнения быстрой сортировки.

    >>> from task1 import quicksort
    >>> quicksort([-1, 0, -5.5, 25, -6])
    [-6, -5.5, -1, 0, 25]
    >>> quicksort([])
    []
    >>> quicksort([4, 4, 1, 5, 1, 6])
    [1, 1, 4, 4, 5, 6]
    >>> quicksort(5)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not subscriptable
