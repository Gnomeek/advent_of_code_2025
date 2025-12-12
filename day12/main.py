import sys

class Present:
    def __init__(self, num: int, shape: list[list[str]]):
        self.num = num
        self.shape = shape
    
    def shape_repr(self):
        rows = []
        for row in self.shape:
            rows.append("".join(row))
        return "\n".join(rows)
        

    def __repr__(self):
        return f"Present {self.num} \n{self.shape_repr()}\n"
    

    def __str__(self):
        return f"Present {self.num} \n{self.shape_repr()}\n"

class Region:
    def __init__(self, size: tuple[int, int], required: list[int]):
        self.size = size
        self.required = required

    
    def __repr__(self):
        return f"Region({self.size}, {self.required})"
    

    def __str__(self):
        return f"Region({self.size}, {self.required})"


def read_input(file_path: str) -> tuple[list[Present], list[Region]]:
    with open(file_path, "r") as file:
        parts = file.read().split("\n\n")
        print(parts[:-1])
        presents = process_presents(parts[:-1])
        regions = process_regions(parts[-1])
        print(presents)
        return presents, regions

def process_presents(strs: list[str]):
    return [process_present(s) for s in strs]

def process_present(s: str):
    lines = s.split("\n")
    idx = int(lines[0][:-1]) # lines[0] = 1: or 2: or 3: etc.
    mat = []
    for line in lines[1:]:
        # line = ### or ##. or #.# etc.
        mat.append(list(line))
    return Present(idx, mat)


def process_regions(s: str) -> list[Region]:
    res = []
    for line in s.split("\n"):
        size_str, required_str = line.split(": ")
        print(size_str, required_str)
        size = tuple([int(i) for i in size_str.split("x")])
        required = [int(i) for i in required_str.split(" ")]
        res.append(Region(size, required))
    return res

def solve_pt1(presents: list[Present], regions: list[Region]) -> int:
    return 0


def solve_pt2(presents: list[Present], regions: list[Region]) -> int:
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        presents, regions = read_input("input_test.txt")
    else:
        presents, regions = read_input("input.txt")
    result_pt1 = solve_pt1(presents, regions)
    result_pt2 = solve_pt2(presents, regions)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")