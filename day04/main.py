from copy import deepcopy
import sys

def read_input(file_path: str) -> list[list[str]]:
    grid = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            grid.append([i for i in line.strip()])
    return grid

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

def neighbors(grid: list[list[str]], x: int, y: int) -> int:
    cnt = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '@':
            cnt += 1
    return cnt
    
    
def solve_pt1(grid: list[list[str]]) -> int:
    res = 0
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@' and neighbors(grid, i, j) < 4:
                res += 1
    return res

def solve_pt2(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])

    neighbor_count = []
    exposed = set()

    for i in range(m):
        row = []
        for j in range(n):
            if grid[i][j] == '.':
                row.append(None)
            else:
                cnt = neighbors(grid, i, j)
                row.append(cnt)
                if cnt < 4:
                    exposed.add((i, j))
        neighbor_count.append(row)
    removed = 0

    while exposed:
        i, j = exposed.pop()
        if neighbor_count[i][j] is None or neighbor_count[i][j] >= 4:
            continue
        neighbor_count[i][j] = None
        removed += 1
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if 0 <= nx < m and 0 <= ny < n and neighbor_count[nx][ny] is not None:
                neighbor_count[nx][ny] -= 1
                if neighbor_count[nx][ny] < 4:
                    exposed.add((nx, ny))
    return removed

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        grid = read_input("input_test.txt")
    else:
        grid = read_input("input.txt")
    result_pt1 = solve_pt1(deepcopy(grid))
    result_pt2 = solve_pt2(deepcopy(grid))
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")