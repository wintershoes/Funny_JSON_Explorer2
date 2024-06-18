from iterator import Iterator
from collections import deque

class Component:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, child):
        self.children.append(child)


class Leaf(Component):
    def __init__(self, name, value):
        self.value = value
        super().__init__(name)


class ComponentIterator:
    def __init__(self, root):
        self.queue = deque([(root, 0, False, False)])

    def __iter__(self):
        return self

    def __next__(self):
        while self.queue:
            node, level, endofparent, startofparent = self.queue.popleft()
            config = (level, endofparent, startofparent)
            if isinstance(node, Composite):
                children = list(node.children)
                for i, child in enumerate(reversed(children)):
                    self.queue.appendleft((child, level + 1, i == 0, i == len(children) - 1))
            return node,config 
        raise StopIteration

class Composite(Component):
    def __init__(self, name):
        super().__init__(name)

    def __iter__(self):
        return ComponentIterator(self)