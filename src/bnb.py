from time import time
from queue import PriorityQueue

from Node import Node
from puzzle import get_empty_position, move, display_puzzle, solvable

# heuristik untuk tidak membangkitkan node dengan konfigurasi yang sama
seen_combination = dict()
# jumlah node yang dibangkitkan
generated_node = 0


def generate_child(puzzle_node: Node) -> list:
    global seen_combination, generated_node
    moved_puzzle = []

    direction_list = ["left", "right", "up", "down"]

    # Kombinasi arah
    for direction in direction_list:
        move_puzzle = move(puzzle_node.get_puzzle(), direction)
        if move_puzzle is not None:
            # Jika move valid, cek apakah konfigurasi ini pernah dibangkitkan
            if not seen_combination.get(str(move_puzzle)):
                generated_node += 1
                seen_combination[str(move_puzzle)] = True
                move_node = Node(move_puzzle, puzzle_node,
                                 puzzle_node.get_depth() + 1, direction)
                moved_puzzle.append(move_node)

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
        min_node = q.get()

    time_stop = time()

    # Lakukan iterasi dari node akhir ke root node
    steps = [min_node]
    parent_node = min_node.get_parent_node()
    while parent_node is not None:
        steps.append(parent_node)
        parent_node = parent_node.get_parent_node()

    steps.reverse()

    for i, node in enumerate(steps):
        print(f"Langkah ke-{i}:")
        display_puzzle(node.get_puzzle())
        print(
            f"arah: {node.get_previous_move() if (node.get_previous_move() is not None) else '-'}\n")

    print("PUZZLE BERHASIL DISELESAIKAN")
    print(f"Waktu eksekusi: {time_stop - time_start} s")
    print(f"Kedalaman / step: {min_node.get_depth()}")
    print(f"Node dibangkitkan: {generated_node}")
    print("Nilai [SIGMA Kurang(i)] + X:", num)
