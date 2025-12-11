from collections import defaultdict
import sys


def read_input(file_path: str) -> dict[str, list[str]]:
    graph = defaultdict(list)
    with open(file_path, "r") as file:
        for line in file.readlines():
            src, dsts = line.strip().split(": ")
            graph[src] = dsts.split(" ")
    return graph

def solve_pt1(graph: dict[str, list[str]]) -> int:
    return 0


def solve_pt2(graph: dict[str, list[str]]) -> int:
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        graph = read_input("input_test.txt")
    else:
        graph = read_input("input.txt")
    result_pt1 = solve_pt1(graph)
    result_pt2 = solve_pt2(graph)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")