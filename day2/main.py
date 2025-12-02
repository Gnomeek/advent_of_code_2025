import sys


def read_input(file_path: str) -> str:
    ranges = []
    with open(file_path, "r") as file:
        for range_str in file.read().strip().split(','):
            start, end = range_str.split('-')
            ranges.append((int(start), int(end)))
    return ranges


def is_invalid_id(num: int) -> bool:
    s = str(num)
    length = len(s)
    if length % 2 != 0:
        return False
    mid = length // 2
    return s[:mid] == s[mid:]


def is_invalid_id_pt2(num: int) -> bool:
    s = str(num)
    length = len(s)
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repeats = length // pattern_len
            if repeats >= 2 and pattern * repeats == s:
                return True
    return False


def solve_pt1(ranges: list[tuple[int, int]]) -> int:
    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total += num
    return total


def solve_pt2(ranges: list[tuple[int, int]]) -> int:
    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id_pt2(num):
                total += num
    return total


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        ranges = read_input("input_test.txt")
    else:
        ranges = read_input("input.txt")
    result_pt1 = solve_pt1(ranges)
    result_pt2 = solve_pt2(ranges)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")
