import random
from collections import defaultdict
import inspect
from ast import *


class Locator(NodeVisitor):
    def __init__(self):
        self.locs = defaultdict(list)

    def visit(self, node):
        self.locs[type(node)].append(node)
        self.generic_visit(node)


class Mutator(NodeTransformer):
    implemented = [BinOp, UnaryOp, BoolOp, Compare]
    mutators_BinOp = {
        Add: [Sub],
        Sub: [Add],
        Mult: [Div, Pow],
        Mod: [Div, FloorDiv]
    }
    mutators_UnaryOp = {
        UAdd: [USub],
        USub: [UAdd]
    }
    mutators_BoolOp = {
        And: [Or],
        Or: [And]
    }
    mutators_Compare = {
        Gt: [GtE, Lt, LtE],
        GtE: [Gt, Lt, LtE],
        Lt: [LtE, Gt, GtE],
        LtE: [Lt, Gt, GtE]
    }

    def __init__(self, locs: defaultdict):
        self.target = None

    def set_target(self, locs: defaultdict):
        node_types = [x for x in list(locs.keys()) if x in Mutator.implemented]

        node_type = random.choice(node_types)
        self.target = random.choice(locs[node_type])

    def visit(self, node):
        if self.target != node:
            return self.generic_visit(node)
        return self.visit_target(node)

    def visit_target(self, node):
        last_op = node.ops[0] if type(node) in [Compare] else node.op
        op = None

        mutators = getattr(Mutator, f'mutators_{type(node).__name__}')
        for key, value in mutators.items():
            if isinstance(last_op, key):
                op = random.choice(value)

        if not op:
            return node
        for x in Mutator.implemented:
            if isinstance(node, x):
                return getattr(self, f'mutator_{x.__name__}')(node, op)

    def mutator_BinOp(self, node, op):
        return copy_location(BinOp(
            left=node.left,
            right=node.right,
            op=op()
        ), node)

    def mutator_UnaryOp(self, node, op):
        return copy_location(UnaryOp(
            operand=node.operand,
            op=op()
        ), node)

    def mutator_BoolOp(self, node, op):
        return copy_location(BoolOp(
            values=node.values,
            op=op()
        ), node)

    def mutator_Compare(self, node, op):
        return copy_location(Compare(
            left=node.left,
            comparators=node.comparators,
            ops=[op()] + node.ops[1:]
        ), node)


def mutate_code(src, max_changes):
    tree = parse(src)
    loc = Locator()
    loc.visit(tree)
    mutator = Mutator(loc.locs)
    for _ in range(random.randint(1, max_changes)):
        mutator.set_target(loc.locs)
        tree = mutator.visit(tree)
    return unparse(tree)


def make_mutants(func, size, max_changes):
    mutant = src = unparse(parse(inspect.getsource(func)))
    mutants = [src]
    while len(mutants) < size + 1:
        attempts = 0
        while mutant in mutants:
            assert attempts < 20, 'Too many failed attempts'
            mutant = mutate_code(src, max_changes)
            attempts += 1
        mutants.append(mutant)
    return mutants[1:]


def mut_test(func, test, size=20, max_changes=3):
    survived, killed = [], []
    mutants = make_mutants(func, size, max_changes)
    for mutant in mutants:
        try:
            exec(mutant, globals())
            test()
            survived.append(mutant)
        except:
            killed.append(mutant)
            pass
    return survived, killed


def fact(n):
    result = 1
    positive = True
    if n < 0:
        n *= -1
        if n % 2:
            positive = False
    while n > 0:
        result *= n
        n -= 1
    if not positive:
        result *= -1
    return result


def test():
    assert fact(7) == 5040
    assert fact(5) == 120
    assert fact(0) == 1
    assert fact(-1) == -1
    assert fact(-2) == 2
    assert fact(-3) == -6
    assert fact(-4) == 24


def main(user_input=False, filename='muttest.log'):
    num, chs = 6, 2
    if user_input:
        num = int(input('Enter number of mutants: '))
        chs = int(input('Enter max number of changes: '))

    try:
        survived, killed = mut_test(fact, test, size=num, max_changes=chs)
    except AssertionError:
        print('Failed to generate unique mutants')
        print('Try to lower the number of mutants')
        return
    surv, dead = len(survived), len(killed)

    with open(filename, 'w') as f:
        f.write('Survived mutants:\n')
        f.write('None.\n' if survived == [] else '-----------------\n')
        count = 1
        for mutant in survived:
            f.write(f'\n--- Survived mutant #{count} ---\n')
            f.write(mutant + '\n')
            count += 1
        count = 1
        f.write('\n\nKilled mutants:\n')
        f.write('None.\n' if killed == [] else '---------------\n')
        for mutant in killed:
            f.write(f'\n--- Killed mutant #{count} ---\n')
            f.write(mutant + '\n')
            count += 1
    print(f'Testing done. Survived: {surv}, killed: {dead}.')
    print(f'See more info in {filename}')


if __name__ == '__main__':
    main(user_input=True)
