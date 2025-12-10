# /// script
# dependencies = [
#   "pulp",
# ]
# ///


from copy import deepcopy
import sys
from collections import deque

class Machine:
    def __init__(self, target, ops, joltage):
        self.curr = "." * len(target)
        self.curr_joltage = tuple([0] * len(joltage))
        self.target = target              
        self.ops = ops
        self.joltage = joltage


    def __str__(self):
        curr_str = "".join(self.curr)
        target_str = "".join(self.target)
        curr_joltage = ",".join(self.curr_joltage)
        target_joltage = ",".join(self.joltage)
        return f"Machine({curr_str} -> {target_str}, {curr_joltage} -> {target_joltage})"


    def __repr__(self):
        curr_str = "".join(self.curr)
        target_str = "".join(self.target)
        curr_joltage = ",".join(self.curr_joltage)
        target_joltage = ",".join(self.joltage)
        return f"Machine({curr_str} -> {target_str}, {curr_joltage} -> {target_joltage})"


def read_input(file_path: str) -> list[Machine]:
    machines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            parts = line.strip().split(" ")
            target = parts[0][1:-1]
            joltage = tuple(int(i) for i in parts[-1][1:-1].split(","))
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
    return sum([pt2(m) for m in machines])

def pt2(machine: Machine) -> int:
    import pulp

    n = len(machine.joltage)
    m = len(machine.ops)

    prob = pulp.LpProblem("Joltage", pulp.LpMinimize)

    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(m)]

    prob += pulp.lpSum(x)

    for pos in range(n):
        expr = pulp.lpSum(x[btn_idx] for btn_idx in range(m) if pos in machine.ops[btn_idx])
        prob += expr == machine.joltage[pos], f"constraint_pos{pos}"

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    if prob.status == pulp.LpStatusOptimal:
        return int(pulp.value(prob.objective))
    else:
        return -1 


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        machines = read_input("input_test.txt")
    else:
        machines = read_input("input.txt")
    result_pt1 = solve_pt1(machines)
    result_pt2 = solve_pt2(machines)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")