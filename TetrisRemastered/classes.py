from __future__ import annotations
from abc import ABC, abstractmethod

class MultiBlock(ABC):
    @abstractmethod
    def copy(self: MultiBlock) -> MultiBlock:
        pass

    @abstractmethod
    def rotate(self: MultiBlock, blocks: list[Block], width: int, height: int) -> None:
        pass

class Block:
    def __init__(self: Block, x: int, y: int, color: tuple[int]=(0,0,0)):
        self.x: int = x
        self.y: int = y
        self.color: tuple = color

    def copy(self: Block) -> Block:
        return Block(self.x, self.y, self.color)

    def __str__(self: Block) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

class O(MultiBlock):
    def __init__(self: O, x: int, y: int) -> None:
        self.blocks: list[Block] = []
        self.blocks.append(Block(x, y, (255, 255, 0)))
        self.blocks.append(Block(x + 1, y, (255, 255, 0)))
        self.blocks.append(Block(x, y + 1, (255, 255, 0)))
        self.blocks.append(Block(x + 1, y + 1, (255, 255, 0)))

    def copy(self: O) -> O:
        block: O = O(self.blocks[0].x, self.blocks[0].y)
        return block

    def rotate(self: O, blocks: list[Block], width: int, height: int) -> None:
        pass

class I(MultiBlock):
    def __init__(self: I, x: int, y: int, rot: int=0):
        self.blocks: list[Block] = []
        self.rot: int = rot
        if rot == 0:
            self.blocks.append(Block(x, y, (0, 255, 255)))
            self.blocks.append(Block(x, y + 1, (0, 255, 255)))
            self.blocks.append(Block(x, y + 2, (0, 255, 255)))
            self.blocks.append(Block(x, y + 3, (0, 255, 255)))
        elif rot == 1:
            self.blocks.append(Block(x, y, (0, 255, 255)))
            self.blocks.append(Block(x - 1, y, (0, 255, 255)))
            self.blocks.append(Block(x - 2, y, (0, 255, 255)))
            self.blocks.append(Block(x - 3, y, (0, 255, 255)))

    def copy(self: I) -> I:
        block: I = I(self.blocks[0].x, self.blocks[0].y, self.rot)
        return block

    def rotate(self: I, blocks: list[Block], width: int, height: int) -> None:
        self.rot += 1
        if self.rot == 2:
            self.rot = 0
        new_block: I = self.copy()
        intersecting: bool = False
        for block in new_block.blocks:
            for placed_block in blocks:
                if block.x == placed_block.x and block.y == placed_block.y:
                    intersecting = True
            if block.y > height/50 - 1:
                intersecting = True
            elif block.x < 0 or block.x > width/50 - 1:
                intersecting = True
        if not intersecting:
            self.blocks = new_block.blocks
        else:
            self.rot -= 1
            if self.rot == -1:
                self.rot = 1

class S(MultiBlock):
    def __init__(self: S, x: int, y: int, rot: int=0):
        self.blocks: list[Block] = []
        self.rot: int = rot
        if rot == 0:
            self.blocks.append(Block(x, y, (0, 255, 0)))
            self.blocks.append(Block(x + 1, y, (0, 255, 0)))
            self.blocks.append(Block(x + 1, y - 1, (0, 255, 0)))
            self.blocks.append(Block(x + 2, y - 1, (0, 255, 0)))
        elif rot == 1:
            self.blocks.append(Block(x, y, (0, 255, 0)))
            self.blocks.append(Block(x, y + 1, (0, 255, 0)))
            self.blocks.append(Block(x + 1, y + 1, (0, 255, 0)))
            self.blocks.append(Block(x + 1, y + 2, (0, 255, 0)))

    def copy(self: S) -> S:
        block: S = S(self.blocks[0].x, self.blocks[0].y, self.rot)
        return block

    def rotate(self: S, blocks: list[Block], width: int, height: int) -> None:
        self.rot += 1
        if self.rot == 2:
            self.rot = 0
        new_block: S = self.copy()
        intersecting: bool = False
        for block in new_block.blocks:
            for placed_block in blocks:
                if block.x == placed_block.x and block.y == placed_block.y:
                    intersecting = True
            if block.y > height/50 - 1:
                intersecting = True
            elif block.x < 0 or block.x > width/50 - 1:
                intersecting = True
        if not intersecting:
            self.blocks = new_block.blocks
        else:
            self.rot -= 1
            if self.rot == -1:
                self.rot = 1

class Z(MultiBlock):
    def __init__(self: Z, x: int, y: int, rot: int=0):
        self.blocks: list[Block] = []
        self.rot: int = rot
        if rot == 0:
            self.blocks.append(Block(x, y, (255, 0, 0)))
            self.blocks.append(Block(x + 1, y, (255, 0, 0)))
            self.blocks.append(Block(x + 1, y + 1, (255, 0, 0)))
            self.blocks.append(Block(x + 2, y + 1, (255, 0, 0)))
        elif rot == 1:
            self.blocks.append(Block(x, y, (255, 0, 0)))
            self.blocks.append(Block(x, y + 1, (255, 0, 0)))
            self.blocks.append(Block(x - 1, y + 1, (255, 0, 0)))
            self.blocks.append(Block(x - 1, y + 2, (255, 0, 0)))

    def copy(self: Z) -> Z:
        block: Z = Z(self.blocks[0].x, self.blocks[0].y, self.rot)
        return block

    def rotate(self: Z, blocks: list[Block], width: int, height: int) -> None:
        self.rot += 1
        if self.rot == 2:
            self.rot = 0
        new_block: Z = self.copy()
        intersecting: bool = False
        for block in new_block.blocks:
            for placed_block in blocks:
                if block.x == placed_block.x and block.y == placed_block.y:
                    intersecting = True
            if block.y > height/50 - 1:
                intersecting = True
            elif block.x < 0 or block.x > width/50 - 1:
                intersecting = True
        if not intersecting:
            self.blocks = new_block.blocks
        else:
            self.rot -= 1
            if self.rot == -1:
                self.rot = 1

class T(MultiBlock):
    def __init__(self: T, x: int, y: int, rot: int=0):
        self.blocks: list[Block] = []
        self.rot: int = rot
        if rot == 0:
            self.blocks.append(Block(x, y + 1, (255, 0, 255)))
            self.blocks.append(Block(x + 1, y + 1, (255, 0, 255)))
            self.blocks.append(Block(x + 1, y, (255, 0, 255)))
            self.blocks.append(Block(x + 2, y + 1, (255, 0, 255)))
        elif rot == 1:
            self.blocks.append(Block(x, y, (255, 0, 255)))
            self.blocks.append(Block(x, y + 1, (255, 0, 255)))
            self.blocks.append(Block(x + 1, y + 1, (255, 0, 255)))
            self.blocks.append(Block(x, y + 2, (255, 0, 255)))
        elif rot == 2:
            self.blocks.append(Block(x, y, (255, 0, 255)))
            self.blocks.append(Block(x + 1, y, (255, 0, 255)))
            self.blocks.append(Block(x + 1, y + 1, (255, 0, 255)))
            self.blocks.append(Block(x + 2, y, (255, 0, 255)))
        elif rot == 3:
            self.blocks.append(Block(x + 1, y, (255, 0, 255)))
            self.blocks.append(Block(x + 1, y + 1, (255, 0, 255)))
            self.blocks.append(Block(x, y + 1, (255, 0, 255)))
            self.blocks.append(Block(x + 1, y + 2, (255, 0, 255)))

    def copy(self: T) -> T:
        block: T
        if self.rot == 0:
            block = T(self.blocks[0].x, self.blocks[0].y - 1, self.rot)
        elif self.rot == 3:
            block = T(self.blocks[0].x - 1, self.blocks[0].y, self.rot)
        else:
            block = T(self.blocks[0].x, self.blocks[0].y, self.rot)
        return block

    def rotate(self: T, blocks: list[Block], width: int, height: int) -> None:
        self.rot += 1
        if self.rot == 4:
            self.rot = 0
        new_block: T = self.copy()
        intersecting: bool = False
        for block in new_block.blocks:
            for placed_block in blocks:
                if block.x == placed_block.x and block.y == placed_block.y:
                    intersecting = True
            if block.y > height/50 - 1:
                intersecting = True
            elif block.x < 0 or block.x > width/50 - 1:
                intersecting = True
        if not intersecting:
            self.blocks = new_block.blocks
        else:
            self.rot -= 1
            if self.rot == -1:
                self.rot = 3

class L(MultiBlock):
    def __init__(self: L, x: int, y: int, rot: int=0):
        self.rot: int = rot
        self.blocks: list[Block] = []
        if rot == 0:
            self.blocks.append(Block(x, y, (255, 125, 0)))
            self.blocks.append(Block(x, y + 1, (255, 125, 0)))
            self.blocks.append(Block(x, y + 2, (255, 125, 0)))
            self.blocks.append(Block(x + 1, y + 2, (255, 125, 0)))
        elif rot == 1:
            self.blocks.append(Block(x + 1, y + 1, (255, 125, 0)))
            self.blocks.append(Block(x, y + 1, (255, 125, 0)))
            self.blocks.append(Block(x - 1, y + 1, (255, 125, 0)))
            self.blocks.append(Block(x - 1, y + 2, (255, 125, 0)))
        elif rot == 2:
            self.blocks.append(Block(x, y - 1, (255, 125, 0)))
            self.blocks.append(Block(x + 1, y - 1, (255, 125, 0)))
            self.blocks.append(Block(x + 1, y, (255, 125, 0)))
            self.blocks.append(Block(x + 1, y + 1, (255, 125, 0)))
        elif rot == 3:
            self.blocks.append(Block(x - 1, y + 1, (255, 125, 0)))
            self.blocks.append(Block(x, y + 1, (255, 125, 0)))
            self.blocks.append(Block(x + 1, y + 1, (255, 125, 0)))
            self.blocks.append(Block(x + 1, y, (255, 125, 0)))

    def copy(self: L) -> L:
        block: L
        if self.rot == 0:
            block = L(self.blocks[0].x, self.blocks[0].y, self.rot)
        elif self.rot == 1:
            block = L(self.blocks[0].x - 1, self.blocks[0].y - 1, self.rot)
        elif self.rot == 2:
            block = L(self.blocks[0].x, self.blocks[0].y + 1, self.rot)
        elif self.rot == 3:
            block = L(self.blocks[0].x + 1, self.blocks[0].y - 1, self.rot)
        return block

    def rotate(self: L, blocks: list[Block], width: int, height: int) -> None:
        self.rot += 1
        if self.rot == 4:
            self.rot = 0
        new_block: L = self.copy()
        intersecting: bool = False
        for block in new_block.blocks:
            for placed_block in blocks:
                if block.x == placed_block.x and block.y == placed_block.y:
                    intersecting = True
            if block.y > height/50 - 1:
                intersecting = True
            elif block.x < 0 or block.x > width/50 - 1:
                intersecting = True
        if not intersecting:
            self.blocks = new_block.blocks
        else:
            self.rot -= 1
            if self.rot == -1:
                self.rot = 3

class J(MultiBlock):
    def __init__(self: J, x: int, y: int, rot: int=0):
        self.rot: int = rot
        self.blocks: list[Block] = []
        if rot == 0:
            self.blocks.append(Block(x, y, (0, 0, 255)))
            self.blocks.append(Block(x, y + 1, (0, 0, 255)))
            self.blocks.append(Block(x, y + 2, (0, 0, 255)))
            self.blocks.append(Block(x - 1, y + 2, (0, 0, 255)))
        elif rot == 1:
            self.blocks.append(Block(x + 1, y + 1, (0, 0, 255)))
            self.blocks.append(Block(x, y + 1, (0, 0, 255)))
            self.blocks.append(Block(x - 1, y + 1, (0, 0, 255)))
            self.blocks.append(Block(x - 1, y, (0, 0, 255)))
        elif rot == 2:
            self.blocks.append(Block(x + 1, y - 1, (0, 0, 255)))
            self.blocks.append(Block(x, y - 1, (0, 0, 255)))
            self.blocks.append(Block(x, y, (0, 0, 255)))
            self.blocks.append(Block(x, y + 1, (0, 0, 255)))
        elif rot == 3:
            self.blocks.append(Block(x - 1, y, (0, 0, 255)))
            self.blocks.append(Block(x, y, (0, 0, 255)))
            self.blocks.append(Block(x + 1, y, (0, 0, 255)))
            self.blocks.append(Block(x + 1, y + 1, (0, 0, 255)))

    def copy(self: J) -> J:
        block: J
        if self.rot == 0:
            block = J(self.blocks[0].x, self.blocks[0].y, self.rot)
        elif self.rot == 1:
            block = J(self.blocks[0].x - 1, self.blocks[0].y - 1, self.rot)
        elif self.rot == 2:
            block = J(self.blocks[0].x - 1, self.blocks[0].y + 1, self.rot)
        elif self.rot == 3:
            block = J(self.blocks[0].x + 1, self.blocks[0].y, self.rot)
        return block

    def rotate(self: J, blocks: list[Block], width: int, height: int) -> None:
        self.rot += 1
        if self.rot == 4:
            self.rot = 0
        new_block: J = self.copy()
        intersecting: bool = False
        for block in new_block.blocks:
            for placed_block in blocks:
                if block.x == placed_block.x and block.y == placed_block.y:
                    intersecting = True
            if block.y > height/50 - 1:
                intersecting = True
            elif block.x < 0 or block.x > width/50 - 1:
                intersecting = True
        if not intersecting:
            self.blocks = new_block.blocks
        else:
            self.rot -= 1
            if self.rot == -1:
                self.rot = 3
