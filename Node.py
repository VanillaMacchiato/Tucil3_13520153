class Node:
    def __init__(self, puzzle: list, parent_index: int, depth: int, previous_move: str = None):
        self._puzzle = puzzle
        self._parent_index = parent_index
        self._depth = depth
        self._cost = depth + self.calculate_g()
        self._expanded = False
        self._previous_move = previous_move

    def calculate_g(self) -> int:
        flattened = flatten(self._puzzle)
        g = 0
        for i in range(16):
            if (flattened[i] != i+1) and (flattened[i] != 0):
                g += 1
        return g

    def get_parent_index(self) -> int:
        return self._parent_index

    def get_puzzle(self):
        return self._puzzle

    def get_cost(self):
        if self._expanded:
            return float("inf")
        return self._cost

    def get_previous_move(self) -> str:
        return self._previous_move

    def get_depth(self) -> int:
        return self._depth

    def is_expanded(self) -> bool:
        return self._expanded

    def debug(self) -> None:
        display_puzzle(self._puzzle)
        print("parent index:", self._parent_index)
        print("cost:", self._cost)
        print("prev move:", self._previous_move)
        print()

    def set_expanded(self, is_expanded: bool) -> None:
        self._expanded = is_expanded


def flatten(puzzle) -> list:
    flattened = []
    for content in puzzle:
        flattened.extend(content)
    return flattened


def display_puzzle(puzzle) -> None:
    for row in puzzle:
        for cell in row:
            if cell < 10:
                if cell == 0:
                    print(" -", end=" ")
                else:
                    print(f" {cell}", end=" ")
            else:
                print(cell, end=" ")
        print()
