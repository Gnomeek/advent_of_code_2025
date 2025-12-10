import sys
from collections import deque

class Machine:
    initial: list[int] = []
    curr: list[int] = []
    target: list[int] = []
    ops: list[list[int]] = []
    joltage: list[int] = []
    def __init__(self, target, ops, joltage):
        self.initial = ["."] * len(target)
        self.curr = ["."] * len(target)
        self.target = target
        self.ops = ops
        self.joltage = joltage


    def __str__(self):
        return f"Machine({"".join(self.curr)})"
    

    def __repr__(self):
        return f"Machine({"".join(self.curr)})"


def read_input(file_path: str) -> list[Machine]:
    machines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            parts = line.strip().split(" ")
            target = list(parts[0][1:-1])
            joltage = parts[-1][1:-1].split(",")
            ops = [part[1:-1].split(",") for part in parts[1:-1]]
            machines.append(Machine(target, ops, joltage))
    return machines

def solve_pt1(machines: list[Machine]) -> int:
    res = 0
    return res


def solve_pt2(machines: list[Machine]) -> int:
    res = 0
    return res


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        machines = read_input("input_test.txt")
    else:
        machines = read_input("input.txt")
    result_pt1 = solve_pt1(machines)
    result_pt2 = solve_pt2(machines)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")