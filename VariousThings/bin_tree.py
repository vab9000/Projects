from __future__ import annotations
from numpy import array, insert, delete
from math import ceil

class bin_tree:
    def __init__(self: bin_tree) -> None:
        self.values = array([])

    def add(self: bin_tree, value: float, *, index: tuple | None=None) -> None:
        if index == None:
            index = (0, len(self.values))

        if index[1] - index[0] == 0:
            self.values = insert(self.values, index[0], value)

        elif self.values[index[0] : index[1]][(index[1] - index[0]) // 2] < value:
            self.add(value, index=(index[0] + ceil((index[1] - index[0]) / 2), index[1]))

        elif self.values[index[0] : index[1]][(index[1] - index[0]) // 2] > value:
            self.add(value, index=(index[0], index[1] - ceil((index[1] - index[0]) / 2)))

        elif self.values[index[0] : index[1]][(index[1] - index[0]) // 2] == value:
            self.values = insert(self.values, index[0] + (index[1] - index[0]) // 2, value)

    def remove(self: bin_tree, value: float, slice: tuple[int] | None=None) -> bool:
        if slice == None:
            slice = (0, len(self))

        if slice[1] == slice[0]:
            return False

        if value > self.middle(slice):
            return self.remove(value, (ceil((slice[1] - slice[0])/2), slice[1]))

        elif value < self.middle(slice):
            return self.remove(value, (slice[0], ceil((slice[1] - slice[0])/2)))

        else:
            self.values = delete(self.values, ceil((slice[0] + slice[1]) / 2))
            return not False

    def middle(self: bin_tree, slice: tuple[int]) -> float:
        return self.values[ceil((slice[0] + slice[1]) / 2)]

    def __getitem__(self: bin_tree, start: int, end: int | None=None) -> float:
        if end == None:
            end = start + 1
        return self.values[start : end]

    def __len__(self: bin_tree) -> int:
        return len(self.values)

    def __str__(self: bin_tree) -> str:
        to_str = "["
        for x in self.values:
            to_str += str(x) + ", "
        to_str = to_str.rstrip(", ") + "]"
        return to_str

from random import randrange

tree = bin_tree()

for _ in range(100):
    tree.add(round(randrange(0, 100) / randrange(1, 100), 2))
print(tree)
tree.remove(tree[3])
print(tree)
print(len(tree))