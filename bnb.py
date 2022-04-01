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

# puzzle = [[0 for j in range(4)] for i in range(4)]


def solvable(puzzle):
    kurang = [0 for _ in range(17)]
    x = 0
    flattened = []
    for content in puzzle:
        flattened.extend(content)
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

print(solvable(instance1))
