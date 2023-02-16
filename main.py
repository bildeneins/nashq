from typing import Tuple
from enum import Enum

# 2つのタプルの要素同士の和
def add_tuple(a, b):
    return tuple([la + lb for (la, lb) in zip(list(a), list(b))])



class Move(Enum):
    UP = (0, 1) 
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    DOWN = (0, -1)

    @property
    def offset(self) -> Tuple[int, int]:
        return self.value

class State:
    Position = Tuple[int, int]
    
    def __init__(self, pos: Position):
        self.pos = pos
    
    """
    m の方向に移動した State を返す
    m は移動できる方向である必要がある（正当な移動であるかチェックを行わない）
    """
    def move(self, m: Move) -> "State":
        return State(add_tuple(self.pos, m.offset))
    
    def __str__(self):
        return str(self.pos)


class Field:
    def __init__(self, H: int = 3, W: int = 3, goal_pos=(1, 2)):
        self.H = H
        self.W = W
        self.goal_pos = goal_pos

class GridWorld:
    def __init__(self, field: Field):
        self.field = field
        self.p1 = State((0, 0))
        self.p2 = State((2, 0))
    
    def render(self):
        for y in reversed(range(self.field.H)):
            for x in range(self.field.W):
                current_pos = (x, y)
                if self.p1.pos == (current_pos):
                    print("A", end="")
                elif self.p2.pos == (current_pos):
                    print("B", end="")
                elif self.field.goal_pos == (current_pos):
                    print("G", end="")
                else:
                    print(" ", end="")
            print("")
        print("")



f = Field()
g = GridWorld(f)
g.render()
g.p1 = g.p1.move(Move.UP)
g.render()