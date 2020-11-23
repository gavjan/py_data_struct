class UNode:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.depth = 1

    def find(self):
        if self is None:
            return None

        ptr = self
        while ptr.parent is not None:
            ptr = ptr.parent

        if ptr != self:
            self.parent = ptr
        return ptr

    def __str__(self):
        return repr(self.val)


def ujoin(a, b):
    if not isinstance(a, UNode) or not isinstance(a, UNode):
        return False

    if a is None or b is None:
        return False

    root_a = a.find()
    root_b = b.find()
    if root_a != root_b:
        if root_a.depth > root_b.depth:
            root_b.parent = root_a
        elif root_a.depth < root_b.depth:
            root_a.parent = root_b
        else:
            root_b.parent = root_a
            root_a.depth += 1

    return root_a != root_b


nodes = {
    "a": UNode(1),
    "b": UNode(2),
    "c": UNode(3),
    "d": UNode(4),
    "e": UNode(5),
    "f": UNode(6)
}

ujoin(nodes["a"], nodes["b"])
ujoin(nodes["b"], nodes["c"])
ujoin(nodes["d"], nodes["e"])
ujoin(nodes["e"], nodes["f"])

for x in nodes:
    print(f"ufind({x}) = {nodes[x].find()}")

ujoin(nodes["c"], nodes["f"])

print("\n--\nAfter Joining:\n")

for x in nodes:
    print(f"ufind({x}) = {nodes[x].find()}")
