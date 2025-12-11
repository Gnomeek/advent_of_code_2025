import sys

def read_input(file_path: str) -> list[list[str]]:
    with open(file_path, "r") as file:
        lines = [line.rstrip('\n\r') for line in file.readlines()]

    if not lines:
        return []

    last_line = lines[-1]
    col_positions = []

    i = 0
    while i < len(last_line):
        if last_line[i] not in (' ', '\t'):
            col_positions.append(i)
            while i < len(last_line) and last_line[i] != ' ':
                i += 1
            while i < len(last_line) and last_line[i] == ' ':
                i += 1
        else:
            i += 1

    col_widths = []
    for i in range(len(col_positions)):
        if i < len(col_positions) - 1:
            width = col_positions[i+1] - col_positions[i] - 1
        else:
            width = len(last_line) - col_positions[i]
        col_widths.append(width)

    grid = []
    for line in lines:
        row = []
        for i, pos in enumerate(col_positions):
            width = col_widths[i]
            col = line[pos:pos+width] if pos < len(line) else ''
            if len(col) < width:
                col = col + ' ' * (width - len(col))
            row.append(col)
        grid.append(row)
    return grid

add = lambda x, y: x + y
multiply = lambda x, y: x * y

def solve_pt1(grid: list[list[str]]) -> int:
    res = 0
    ROWS, COLS = len(grid), len(grid[0])
    for j in range(COLS):
        op = add if grid[-1][j].strip() == "+" else multiply
        temp = 0 if grid[-1][j].strip() == "+" else 1
        vals = []
        for i in range(ROWS-1):
            temp = op(temp, int(grid[i][j]))
        res += temp
    return res

def solve_pt2(grid: list[list[str]]) -> int:
    res = 0
    ROWS, COLS = len(grid), len(grid[0])
    for j in range(COLS):
        op = add if grid[-1][j].strip() == "+" else multiply
        temp = 0 if grid[-1][j].strip() == "+" else 1
        vals = []
        for digits in zip(*[grid[i][j] for i in range(ROWS-1)]):
            vals.append(int(''.join(digits).strip()))
        for v in vals:
            temp = op(temp, v)
        res += temp
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