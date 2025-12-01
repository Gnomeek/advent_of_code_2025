from enum import Enum
import sys


class Direction(Enum):
    LEFT = 1
    RIGHT = 2


class Move:
    direction: Direction
    steps: int

    def __init__(self, direction: str, steps: str) -> None:
        self.direction = Direction.LEFT if direction == "L" else Direction.RIGHT
        self.steps = int(steps)

    def __str__(self) -> str:
        return f"{self.direction} {self.steps}"

    def __repr__(self) -> str:
        return f"Move(direction={self.direction}, steps={self.steps})"

def read_input(file_path: str) -> list[Move]:
    with open(file_path, "r") as file:
        return [Move(line[0], line[1:]) for line in file.readlines()]


def simulate_moves_pt1(moves: list[Move]) -> int:
    position = 50
    res = 0
    for move in moves:
        if move.direction == Direction.RIGHT:
            position = (move.steps + position) % 100
        else:
            position = (position - move.steps + 100) % 100
        if position == 0:
            res += 1
    return res

def simulate_moves_pt2(moves: list[Move]) -> int:
    position = 50
    res = 0
    for move in moves:
        if move.direction == Direction.RIGHT:
            res += (position + move.steps) // 100
            position = (position + move.steps) % 100
        else:
            # Count how many times we pass through or land on 0 going counter-clockwise
            if position != 0:
                # Count crossings when moving left from non-zero position
                if move.steps >= position:
                    res += (move.steps - position) // 100 + 1
            else:
                # Starting at 0, only count if we make full rotations backwards
                res += move.steps // 100
            position = (position - move.steps) % 100
    return res

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        moves = read_input("input_test.txt")
    else:
        moves = read_input("input.txt")
    result_pt1 = simulate_moves_pt1(moves)
    result_pt2 = simulate_moves_pt2(moves)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")