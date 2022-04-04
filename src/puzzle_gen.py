import random

from puzzle import display_puzzle, move, get_empty_position


def generate(depth: int = 10):
    state = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 0]]

    move_list = ["up", "right", "down", "left"]

    realized_move = []

    new_state = state
    while len(realized_move) < depth:
        move_direction = random.choice(move_list)
        status = move(new_state, move_direction)
        if status is not None:
            new_state = status
            realized_move.append(move_direction)
        
        

    return new_state


def generate_menu():
    print("\n>>15-PUZZLE GENERATOR<<\n")

    puzzle = []
    success = False
    print("Masukkan jumlah step mengacak puzzle.")
    depth = input("Step: ")
    try:
        depth = int(depth)
        if depth < 0:
            print("Bukan angka yang valid!")
        elif depth > 50:
            print("Step terlalu besar!")
        elif depth < 2:
            print("Step terlalu kecil!")
        else:
            puzzle = generate(depth)
            print("\nPuzzle berhasil dibangkitan.")
            display_puzzle(puzzle)
            confirm = input("\nProses puzzle ini (Y/N)? ")
            if confirm.lower() == "y":
                success = True
            else:
                print("Proses dibatalkan")
    except:
        print("Bukan angka yang valid!")

    return (success, puzzle)