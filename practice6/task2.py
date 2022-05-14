def person(name, age):
    def getter(key):
        if key == 'name':
            return name
        return age

    return getter


def replace(p, key, value):
    new_name = p('name')
    new_age = p('age')

    if key == 'name':
        new_name = value
    else:
        new_age = value

    return person(new_name, new_age)


def get(p, key):
    return p(key)


if __name__ == '__main__':
    p1 = person(name='Иван', age=20)
    p2 = replace(replace(p1, 'name', 'Алексей'), 'age', 21)
    print(get(p1, 'name'), get(p1, 'age'))
    print(get(p2, 'name'), get(p2, 'age'))
