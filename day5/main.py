import sys

def read_input(file_path: str) -> tuple[list[list[int]], list[int]]:
    data = []
    intervals = []
    interval_end = False
    with open(file_path, "r") as file:
        for line in file.readlines():
            if line.strip() == "":
                interval_end = True
                continue
            if not interval_end:
                a, b = line.strip().split("-")
                intervals.append([int(a), int(b)])
            else:
                data.append(int(line.strip()))
    return intervals, data
    
def solve_pt1(intervals: list[list[int]], data: list[int]) -> int:
    res = 0
    for start, end in intervals:
        for i in data:
            if start <= i <= end:
                res += 1
                continue
    return res


def solve_pt2(intervals: list[list[int]]) -> int:
    print(intervals)
    res = 0
    for start, end in intervals:
        res += (end - start + 1)
    return res

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []
    s, e = intervals[0]
    for start, end in intervals[1:]:
        if start > e:
            merged_intervals.append([s, e])
            s, e = start, end
        else:
            e = max(e, end)
            s = min(s, start)
    merged_intervals.append([s, e])
    return merged_intervals

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        intervals, data = read_input("input_test.txt")
    else:
        intervals, data = read_input("input.txt")
    merged_intervals = merge_intervals(intervals)
    result_pt1 = solve_pt1(merged_intervals, data)
    result_pt2 = solve_pt2(merged_intervals)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")