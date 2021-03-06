from read_input import parse_console, parse_file
from bnb import solve_15_puzzle
from puzzle_gen import generate, generate_menu


def print_help():
    print(">>> Command tersedia <<<")
    print("help: Menampilkan menu ini")
    print("file: Melakukan load puzzle dari file")
    print("type: Melakukan load puzzle dari input console")
    print("gen: Melakukan pembangkitan acak oleh program")
    print("exit: Mengakhiri program")


def main():
    print("--- 15-PUZZLE SOLVER ---")
    print("supported by branch and bound algorithm\n")
    print_help()

    cmd = input("\n> ")
    while cmd != "exit":
        if cmd == "file":
            success, puzzle = parse_file()
            if success:
                solve_15_puzzle(puzzle)
        elif cmd == "type":
            success, puzzle = parse_console()
            if success:
                solve_15_puzzle(puzzle)
        elif cmd == "exit":
            pass
        elif cmd == "help":
            print_help()
        elif cmd == "gen":
            success, puzzle = generate_menu()
            if success:
                solve_15_puzzle(puzzle)
        else:
            print("Command tidak diketahui!")
        cmd = input("\n> ")

    print("Terima kasih telah menggunakan program 15-puzzle solver :)")


main()
