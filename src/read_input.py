from Node import display_puzzle


def parse_puzzle(puzzle_raw: list[str]):
    valid = True
    puzzle = []
    
    # Validasi puzzle dengan dictionary yang me-mapping dari 0 hingga 16
    number_map = dict([(str(x), 0) for x in range(16)])

    if len(puzzle_raw) != 4:
        valid = False
    else:
        for k in puzzle_raw:
            row = k.strip().split(" ")
            for cell in row:
                res = number_map.get(cell)
                if res is None or res > 0:
                    valid = False
                    break
                else:
                    number_map[cell] = 1
            puzzle.append([int(x) for x in row])
    return (valid, puzzle)


def parse_file():
    print("\n>>INPUT 15-PUZZLE DARI FILE<<")
    print("Contoh: test/instance1.txt, instance1.txt")
    filename = input("Masukkan nama file: ")
    
    success = False
    puzzle = []
    try:
        with open(filename, "r") as f:
            valid, puzzle = parse_puzzle(f.readlines())
            if valid:
                print("Puzzle berhasil di-parse! Berikut konfigurasi puzzle yang terdeteksi:\n")
                display_puzzle(puzzle)
                confirm = input("\nProses puzzle ini (Y/N)? ")
                if confirm.lower() == "y":
                    success = True
                else:
                    print("Proses dibatalkan")
            else:
                print("Konfigurasi puzzle tidak valid!")
    except FileNotFoundError:
        print("File tidak ditemukan!")

    return (success, puzzle)

def parse_console():
    print(">>INPUT 15-PUZZLE DARI CONSOLE<<")
    print("Pisahkan kolom dengan spasi; Pisahkan baris dengan enter.")
    print("Substitusi tile kosong dengan angka 0.")

    puzzle = []
    puzzle_raw = []
    success = False
    for i in range(4):
        row = input(f"[{i+1}]: ")
        puzzle_raw.append(row)

    # Validasi puzzle dengan dictionary yang me-mapping dari 0 hingga 16
    valid, puzzle = parse_puzzle(puzzle_raw)

    if not valid:
        print("Konfigurasi puzzle yang di-input tidak valid!")
    else:
        print("Puzzle berhasil di-parse! Berikut konfigurasi puzzle yang terdeteksi:\n")
        display_puzzle(puzzle)
        confirm = input("\nProses puzzle ini (Y/N)? ")
        if confirm.lower() == "y":
            success = True
        else:
            print("Proses dibatalkan")

    return (success, puzzle)    
    
