import sys
from collections import deque


class Dot:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def diff_x(self, another: 'Dot'):
        return abs(self.x - another.x)

    def diff_y(self, another: 'Dot'):
        return abs(self.y - another.y)


def read_input(file_path: str) -> list[Dot]:
    pos = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            vals = line.strip().split(",")
            pos.append(Dot(vals[0], vals[1]))
    return pos

def solve_pt1(positions: list[Dot]) -> int:
    res, n = 0, len(positions)
    for i in range(n):
        for j in range(i+1, n):
            width = positions[i].diff_x(positions[j]) + 1
            height = positions[i].diff_y(positions[j]) + 1
            res = max(res, width*height)
    return res


def solve_pt2(positions: list[Dot]) -> int:
    n = len(positions)

    xs = sorted(set([0, sys.maxsize] + [p.x for p in positions]))
    ys = sorted(set([0, sys.maxsize] + [p.y for p in positions]))

    shrink_x = {x: i for i, x in enumerate(xs)}
    shrink_y = {y: i for i, y in enumerate(ys)}

    width, height = len(xs), len(ys)
    grid = [['X'] * width for _ in range(height)]

    for i in range(n):
        x1, y1 = positions[i].x, positions[i].y
        x2, y2 = positions[(i + 1) % n].x, positions[(i + 1) % n].y
        cx1, cy1 = shrink_x[x1], shrink_y[y1]
        cx2, cy2 = shrink_x[x2], shrink_y[y2]
        for cx in range(min(cx1, cx2), max(cx1, cx2) + 1):
            for cy in range(min(cy1, cy2), max(cy1, cy2) + 1):
                grid[cy][cx] = '#'
    queue = deque([(0, 0)])
    grid[0][0] = '.'

    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] == 'X':
                grid[ny][nx] = '.'
                queue.append((ny, nx))
    res = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = positions[i].x, positions[i].y
            x2, y2 = positions[j].x, positions[j].y

            cx1, cy1 = shrink_x[x1], shrink_y[y1]
            cx2, cy2 = shrink_x[x2], shrink_y[y2]

            valid = True
            for cx in range(min(cx1, cx2), max(cx1, cx2) + 1):
                for cy in range(min(cy1, cy2), max(cy1, cy2) + 1):
                    if grid[cy][cx] == '.':
                        valid = False
                        break
                if not valid:
                    break

            if valid:
                area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
                res = max(res, area)

    return res


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        positions = read_input("input_test.txt")
    else:
        positions = read_input("input.txt")
    result_pt1 = solve_pt1(positions)
    result_pt2 = solve_pt2(positions)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")