from copy import deepcopy
import sys
from collections import deque

class Machine:
    curr: list[int] = []
    target: list[int] = []
    ops: list[list[int]] = []
    joltage: list[int] = []
    used_ops: list[bool] = []


    def __init__(self, target, ops, joltage, curr=None, used_ops=None):
        self.curr = ["."] * len(target) if not curr else curr
        self.target = target
        self.ops = ops
        self.used_ops = [False] * len(ops) if not used_ops else used_ops
        self.joltage = joltage

    
    def can_flip_by_op(self, op_idx) -> bool:
        return not self.used_ops[op_idx]


    def flip_by_op(self, op_idx: int) -> 'Machine':
        curr = self.curr.copy()
        used_ops = self.used_ops.copy()
        for i in self.ops[op_idx]:
            if curr[i] == ".":
                curr[i] = "#"
            else:
                curr[i] = "."
        for idx in range(len(used_ops)):
            if idx == op_idx:
                used_ops[idx] = True
            else:
                used_ops[idx] = False
        return Machine(self.target, self.ops, self.joltage, curr, used_ops)
    

    def is_reach_target(self) -> bool:
        for c, t in zip(self.curr, self.target):
            if c != t:
                return False
        return True


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
            target = list(parts[0][1:-1])
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
    res = 0
    for idx, machine in enumerate(machines):
        temp = pt1(machine)
        print(idx, temp)
        res += temp
    return res

def pt1(machine: Machine) -> int:
    res = 0
    queue: list[Machine] = [machine]
    while queue:
        res += 1
        size = len(queue)
        for _ in range(size):
            curr = queue.pop(0)
            for idx, op in enumerate(curr.ops):
                if not curr.can_flip_by_op(idx):
                    continue
                fliped = curr.flip_by_op(idx)
                queue.append(fliped)
                if fliped.is_reach_target():
                    return res 


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