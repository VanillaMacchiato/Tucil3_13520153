class Node:
    def __init__(self, puzzle: list, parent_node, depth: int, previous_move: str = None):
        self._puzzle = puzzle
        self._parent_node = parent_node
        self._depth = depth
        self._cost = depth + self.calculate_g()  # c(P) = f(P) + g(P)
        self._previous_move = previous_move

    def calculate_g(self) -> int:
        flattened = flatten(self._puzzle)
        g = 0
        for i in range(16):
            if (flattened[i] != i+1) and (flattened[i] != 0):
                g += 1
        return g

    def get_parent_node(self):
        return self._parent_node

    def get_puzzle(self) -> list:
        return self._puzzle

    def get_cost(self) -> int:
        return self._cost

    def get_previous_move(self) -> str:
        return self._previous_move

    def get_depth(self) -> int:
        return self._depth

    def debug(self) -> None:
        display_puzzle(self._puzzle)
        print("cost:", self._cost)
        print("prev move:", self._previous_move)
        print()

    # operasi less than (<) untuk priority queue
    def __lt__(self, other) -> bool:
        return self.get_cost() < other.get_cost()


def flatten(puzzle) -> list:
    # Mengubah puzzle 2D menjadi 1D
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
