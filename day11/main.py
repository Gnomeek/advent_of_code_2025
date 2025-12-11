from collections import defaultdict
import sys


START, OUT = "you", "out"
SVR, DAC, FFT = "svr", "dac", "fft"

def read_input(file_path: str) -> dict[str, list[str]]:
    graph = defaultdict(list)
    with open(file_path, "r") as file:
        for line in file.readlines():
            src, dsts = line.strip().split(": ")
            graph[src] = dsts.split(" ")
    return graph


def solve_pt1(graph: dict[str, list[str]]) -> int:
    return path_count(graph, START, OUT)


def solve_pt2(graph: dict[str, list[str]]) -> int:
    """
    case 1: SVR -...-> DAC -...-> FFT -...-> OUT
    case 2: SVR -...-> FFT -...-> DAC -...-> OUT
    it's guaranteed there's no cycle in graph
    """
    SVR2DAC = path_count(graph, SVR, DAC)
    DAC2FFT = path_count(graph, DAC, FFT)
    FFT2OUT = path_count(graph, FFT, OUT)

    SVR2FFT = path_count(graph, SVR, FFT)
    FFT2DAC = path_count(graph, FFT, DAC)
    DAC2OUT = path_count(graph, DAC, OUT)
    
    case_1 = SVR2DAC * DAC2FFT * FFT2OUT
    case_2 = SVR2FFT * FFT2DAC * DAC2OUT
    return case_1 + case_2


def path_count(graph, src, dst):
    memo = {}
    def dfs(curr, target):
        if curr == target:
            return 1
        if curr in memo:
            return memo[curr]
        total = 0
        for adj in graph[curr]:
            total += dfs(adj, target)
        memo[curr] = total
        return total
    return dfs(src, dst)



if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        if len(sys.argv) > 2 and sys.argv[2] == "pt2":
            graph = read_input("input_test_pt2.txt")
        else:
            graph = read_input("input_test.txt")
    else:
        graph = read_input("input.txt")
    result_pt1 = solve_pt1(graph)
    result_pt2 = solve_pt2(graph)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")