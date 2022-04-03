from copy import deepcopy
from time import time
from Node import Node, flatten, display_puzzle

# Instansiasi list of list sebagai permasalahan 15-puzzle
# unsolvable
instance1 = [[1, 3, 4, 15],
             [2, 0, 5, 12],
             [7, 6, 11, 14],
             [8, 9, 10, 13]]

# solvable
instance2 = [[1, 2, 3, 4],
             [5, 6, 0, 8],
             [9, 10, 7, 11],
             [13, 14, 15, 12]]
# unsolvable
instance3 = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 15, 14, 0]]

# solvable (10 steps)
instance4 = [[5, 1, 3, 4],
             [9, 2, 7, 8],
             [0, 6, 15, 11],
             [13, 10, 14, 12]]

# solvable (20 steps)
instance5 = [[1, 6, 2, 4],
             [5, 0, 3, 8],
             [9, 7, 15, 11],
             [13, 14, 10, 12]]

# solvable (30 steps)
instance6 = [[5, 2, 8, 10],
             [1, 11, 6, 4],
             [7, 9, 0, 3],
             [13, 14, 15, 12]]

seen_combination = dict()


def solvable(puzzle) -> bool:
    kurang = [0 for _ in range(17)]
    x = 0
    flattened = flatten(puzzle)
    for index, i in enumerate(flattened):
        if i == 0:
            i = 16
            # Menentukan sel kosong di tempat arsir atau tidak
            index_row = index // 4
            index_col = index % 4
            if (index_row + index_col % 2) == 1:
                x = 1
        temp = 0
        for j in flattened[index+1:]:
            if j < i and j != 0:
                temp += 1
        kurang[i] = temp

    return (sum(kurang) + x) % 2 == 0


def get_empty_position(puzzle) -> tuple:
    for row_index, row in enumerate(puzzle):
        for col_index, cell in enumerate(row):
            if cell == 0:
                return (row_index, col_index)


def move(puzzle: list, empty_position: tuple, direction: str) -> list:
    empty_row = empty_position[0]
    empty_col = empty_position[1]
    
    x_mod = 0
    y_mod = 0

    if direction == "up":
        if empty_row == 0:
            return
        y_mod = -1
    elif direction == "down":
        if empty_row == 3:
            return
        y_mod = 1
    elif direction == "left":
        if empty_col == 0:
            return
        x_mod = -1
    elif direction == "right":
        if empty_col == 3:
            return
        x_mod = 1

    puzzle_copy = deepcopy(puzzle)

    # Melakukan perubahan posisi
    tmp = puzzle_copy[empty_row + y_mod][empty_col + x_mod]
    puzzle_copy[empty_row + y_mod][empty_col + x_mod] = 0
    puzzle_copy[empty_row][empty_col] = tmp
    return puzzle_copy


def generate_child(puzzle_node: Node, parent_index: int) -> list:
    global seen_combination
    moved_puzzle = []
    moved_cost = []

    row, col = get_empty_position(puzzle_node.get_puzzle())
    direction_list = ["left", "right", "up", "down"]

    # Kombinasi arah
    for direction in direction_list:
        move_puzzle = move(puzzle_node.get_puzzle(), (row, col), direction)
        if move_puzzle is not None:
            move_node = Node(move_puzzle, parent_index,
                             puzzle_node.get_depth() + 1, direction)
            move_cost = move_node.get_cost()
            if not seen_combination.get(str(move_node.get_puzzle())):
                moved_puzzle.append(move_node)
                moved_cost.append(move_cost)
                seen_combination[str(move_node.get_puzzle())] = True
    return (moved_puzzle, moved_cost)


def solve_15_puzzle(puzzle):
    print("\n15-PUZZLE SOLVER STARTING...\n")

    time_start = time()
    if not solvable(puzzle):
        print("Konfigurasi ini tidak dapat diselesaikan")
        return

    q: list[Node] = []
    costs: list[int] = []

    rootNode = Node(puzzle, -1, 0, None)
    rootNode.set_expanded(True)

    q.append(rootNode)
    costs.append(rootNode.get_cost())

    children_node, children_cost = generate_child(rootNode, 0)
    q.extend(children_node)
    costs.extend(children_cost)

    min_index, min_value = min(enumerate(costs), key=lambda x: x[1])
    g = q[min_index].calculate_g()

    time_min_node = 0
    time_generate = 0
    limit = 0
    while (g > 0):
        time_generate_child = time()
        children_node, children_cost = generate_child(q[min_index], min_index)
        q[min_index].set_expanded(True)
        costs[min_index] = float("inf")
        q.extend(children_node)
        costs.extend(children_cost)

        time_generate += time() - time_generate_child
        time_node = time()
        min_index, min_value = min(enumerate(costs), key=lambda x: x[1])
        g = q[min_index].calculate_g()
        time_min_node += time() - time_node

    time_stop = time()

    solution = q[min_index]
    solution_path: list[Node] = [solution]
    while (solution.get_parent_index() != -1):
        solution = q[solution.get_parent_index()]
        solution_path.append(solution)

    solution_path.reverse()

    for node in solution_path:
        display_puzzle(node.get_puzzle())
        print()
    print(
        f"Time to find min node: {time_min_node} s; Time to generate child: {time_generate} s")
    print(f"Waktu eksekusi: {time_stop - time_start} s")
    print(f"Kedalaman / step: {len(solution_path)}")
    print(f"Node dibangkitkan: {len(q)}")


if __name__ == "__main__":
    solve_15_puzzle(instance6)