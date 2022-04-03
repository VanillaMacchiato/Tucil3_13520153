from copy import deepcopy
from time import time
from Node import Node, flatten, display_puzzle
from queue import PriorityQueue

# heuristik untuk tidak membangkitkan node dengan konfigurasi yang sama
seen_combination = dict()
generated_node = 0


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
    print("-- Fungsi KURANG(i) -- ")
    for i in range(1, 17):
        print(f"{i}: {kurang[i]}")
    print()
    return sum(kurang) + x


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


def generate_child(puzzle_node: Node) -> list:
    global seen_combination, generated_node
    moved_puzzle = []

    row, col = get_empty_position(puzzle_node.get_puzzle())
    direction_list = ["left", "right", "up", "down"]

    # Kombinasi arah
    for direction in direction_list:
        move_puzzle = move(puzzle_node.get_puzzle(), (row, col), direction)
        if move_puzzle is not None:
            move_node = Node(move_puzzle, puzzle_node,
                             puzzle_node.get_depth() + 1, direction)
            if not seen_combination.get(str(move_node.get_puzzle())):
                generated_node += 1
                moved_puzzle.append(move_node)
                seen_combination[str(move_node.get_puzzle())] = True
    return moved_puzzle


def solve_15_puzzle(puzzle):
    # Me-reset seen_combination dan generated_node
    global seen_combination, generated_node
    seen_combination = dict()
    generated_node = 0
    print("\n15-PUZZLE SOLVER STARTING...\n")

    time_start = time()
    num = solvable(puzzle)
    if not num % 2 == 0:
        print("Konfigurasi ini tidak dapat diselesaikan.")
        print("Nilai [SIGMA Kurang(i)] + X:", num)
        return

    q = PriorityQueue()

    root_node = Node(puzzle, None, 0, None)
    if (root_node.calculate_g() == 0):
        print("Puzzle sudah berada pada posisi solusi!")
        return

    min_node = root_node
    # Selama goal node belum tercapai, lakukan iterasi untuk mencari node hingga g = 0
    while (min_node.calculate_g() > 0):
        child_nodes = generate_child(min_node)
        for node in child_nodes:
            q.put(node)
        min_node: Node = q.get()

    time_stop = time()

    # step tidak
    steps = [min_node]
    parent_node = min_node.get_parent_node()
    while parent_node.get_parent_node() is not None:
        steps.append(parent_node)
        parent_node = parent_node.get_parent_node()

    steps.reverse()

    for node in steps:
        display_puzzle(node.get_puzzle())
        print(f"arah: {node.get_previous_move()}\n")

    print("PUZZLE BERHASIL DISELESAIKAN")
    print(f"Waktu eksekusi: {time_stop - time_start} s")
    print(f"Kedalaman / step: {min_node.get_depth()}")
    print(f"Node dibangkitkan: {generated_node}")
    print("Nilai [SIGMA Kurang(i)] + X:", num)

