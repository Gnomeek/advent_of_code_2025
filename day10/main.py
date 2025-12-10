from copy import deepcopy
import sys
from collections import deque

class Machine:
    def __init__(self, target, ops, joltage):
        self.curr = "." * len(target)
        self.target = target              
        self.ops = ops
        self.joltage = joltage


    def __str__(self):
        curr_str = "".join(self.curr)
        target_str = "".join(self.target)
        return f"Machine({curr_str} -> {target_str})"


    def __repr__(self):
        curr_str = "".join(self.curr)
        target_str = "".join(self.target)
        return f"Machine({curr_str} -> {target_str})"


def read_input(file_path: str) -> list[Machine]:
    machines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            parts = line.strip().split(" ")
            target = parts[0][1:-1]
            joltage = [int(i) for i in parts[-1][1:-1].split(",")]
            ops = []
            for part in parts[1:-1]:
                temp = []
                for i in part[1:-1].split(","):
                    temp.append(int(i))
                ops.append(temp)
            machines.append(Machine(target, ops, joltage))
    return machines

def solve_pt1(machines: list[Machine]) -> int:
    return sum([pt1(m) for m in machines])

def pt1(machine: Machine) -> int:
    initial = machine.curr
    target = machine.target

    if initial == target:
        return 0

    visited = {initial}
    queue = deque([(initial, 0)])

    while queue:
        curr, steps = queue.popleft()

        for op in machine.ops:
            state = list(curr)
            for i in op:
                state[i] = '#' if state[i] == '.' else '.'
            next_state = "".join(state)

            if next_state in visited:
                continue

            visited.add(next_state)
            if next_state == target:
                return steps + 1

            queue.append((next_state, steps + 1))

    return -1 


def solve_pt2(machines: list[Machine]) -> int:
    res = 0
    return res


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        machines = read_input("input_test.txt")
        # machines = read_input("day10/input_test.txt")
    else:
        machines = read_input("input.txt")
    result_pt1 = solve_pt1(machines)
    result_pt2 = solve_pt2(machines)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")