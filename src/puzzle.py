from copy import deepcopy


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


def get_empty_position(puzzle: list) -> tuple:
    for row_index, row in enumerate(puzzle):
        for col_index, cell in enumerate(row):
            if cell == 0:
                return (row_index, col_index)


def move(puzzle: list, direction: str) -> list:
    empty_row, empty_col = get_empty_position(puzzle)

    x_mod = 0
    y_mod = 0

    # Jika direction tidak valid, return None
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

    # Melakukan perubahan posisi antara tile kosong dengan tile sebelahnya
    tmp = puzzle_copy[empty_row + y_mod][empty_col + x_mod]
    puzzle_copy[empty_row + y_mod][empty_col + x_mod] = 0
    puzzle_copy[empty_row][empty_col] = tmp
    return puzzle_copy
