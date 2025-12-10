import sys


def read_input(file_path: str):
    with open(file_path, "r") as file:
        pass
    return []

def solve_pt1(x) -> int:
    return 0


def solve_pt2(x) -> int:
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        x = read_input("input_test.txt")
    else:
        x = read_input("input.txt")
    result_pt1 = solve_pt1(x)
    result_pt2 = solve_pt2(x)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")