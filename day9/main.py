import sys

class Dot(object):
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
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        positions = read_input("input_test.txt")
    else:
        positions = read_input("input.txt")
    result_pt1 = solve_pt1(positions)
    result_pt2 = solve_pt2(positions)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")