class File:
    def __init__(self, name, parent, size=None):
        self.name = name
        self._size = size
        self.parent = parent

    @property
    def size(self):
        return self._size

    def traverse(self):
        yield self

    def __str__(self):
        return f"{self.name}\t{self.size}"


class Directory(File):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def get_child(self, name):
        for child in self._children:
            if child.name == name:
                return child
        raise ValueError(f"No child with name {name} found")

    @property
    def size(self):
        return sum(file.size for file in self._children)

    def traverse(self):
        for child in self._children:
            for grandchild in child.traverse():
                yield grandchild
        yield self
