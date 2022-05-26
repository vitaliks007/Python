class Node:
    dash_l = None
    snap_l = None
    scrub_l = None
    dash_val = None
    snap_val = None
    scrub_val = None


class Link:
    node = None

    def __init__(self, node):
        self.node = node

    def dash(self):
        if self.node.dash_l is None:
            raise KeyError
        value = self.node.dash_val
        self.node = self.node.dash_l
        return value

    def snap(self):
        if self.node.snap_l is None:
            raise KeyError
        value = self.node.snap_val
        self.node = self.node.snap_l
        return value

    def scrub(self):
        if self.node.scrub_l is None:
            raise KeyError
        value = self.node.scrub_val
        self.node = self.node.scrub_l
        return value


def main():
    root = Node()

    root.dash_val = 1
    root.dash_l = root

    root.snap_val = 0
    root.snap_l = Node()
    last = root.snap_l

    last.dash_val = 3
    last.dash_l = Node()
    last = last.dash_l

    last.scrub_val = 4
    last.scrub_l = Node()
    last = last.scrub_l

    root.scrub_val = 2
    root.scrub_l = Node()

    last.snap_val = 6
    last.snap_l = last

    last.dash_val = 5
    last.dash_l = Node()
    last = last.dash_l
    curr = last

    last.dash_val = 7
    last.dash_l = Node()
    last = last.dash_l

    last.scrub_val = 9
    last.scrub_l = Node()
    last = last.scrub_l

    curr.scrub_val = 8
    curr.scrub_l = last

    return Link(root)


o = main()
print(o.dash())  # 1
print(o.snap())  # 0
print(o.snap())  # KeyError
print(o.dash())  # 3
print(o.scrub())  # 4
print(o.snap())  # 6
print(o.dash())  # 5
print(o.dash())  # 7
print(o.scrub())  #9
