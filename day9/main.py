import sys

def read_input(file_path: str):
    with open(file_path, "r") as file:
        pass


def solve_pt1(grid: list[list[str]]) -> int:
    res = 0
    return res

def solve_pt2(grid: list[list[str]]) -> int:
    res = 0
    return res


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        grid = read_input("input_test.txt")
    else:
        grid = read_input("input.txt")
    result_pt1 = solve_pt1(grid)
    result_pt2 = solve_pt2(grid)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")