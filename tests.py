def _add(node, v):
    new = [v, [], []]
    if node:
        left, right = node[1:]
        if not left:
            print(left, "not left")
            left.extend(new)
        elif not right:
            print(right, "not right")
            right.extend(new)
        else:
            _add(left, v)
    else:
       node.extend(new)

def binary_tree(s):
    root = []
    for e in s:
        _add(root, e)
    return root

def calc_higth(tree):
   # max_higth = 1/4
    if tree:
        left, right = tree[1:]
        if left:
            return 1 + calc_higth(left)
        else:
            return 0
    else:
        return 0

t = binary_tree('A B C D E F'.split())
print(t)
print(calc_higth(t))

#['A', ['B', ['D', ['F', [], []], ['G', [], []]], ['E', [], []]], ['C', [], []]]






























