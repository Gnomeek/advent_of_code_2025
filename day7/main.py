import sys

def read_input(file_path: str) -> list[list[str]]:
    grid = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            temp = [c for c in line.strip()]
            grid.append(temp)
    return grid


def solve_pt1(grid: list[list[str]]) -> int:
    res = 0
    beam_idx = set()
    for i, c in enumerate(grid[0]):
        if c == "S":
            beam_idx.add(i)
            break
    for i in range(len(grid) - 1):
        for j in beam_idx.copy():
            if grid[i+1][j] == "^":
                res += 1
                beam_idx.remove(j)
                beam_idx.add(j-1)
                beam_idx.add(j+1)
    return res

def solve_pt2(grid: list[list[str]]) -> int:
    # dfs backtracking
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