import sys

def read_input(file_path: str) -> list[list[int]]:
    banks = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            banks.append([int(i) for i in line.strip()])
    return banks
    
def solve_pt1(banks: list[list[int]]) -> int:
    total = 0
    for bank in banks:
        l, left_most = 0, 0
        while l < len(bank) - 1:
            if bank[l] > bank[left_most]:
                left_most = l
            l += 1
        r, right_most = len(bank) - 1, len(bank) - 1
        while r > left_most:
            if bank[r] > bank[right_most]:
                right_most = r
            r -= 1
        res = bank[left_most] * 10 + bank[right_most]
        total += res
    return total

def solve_pt2(banks: list[list[int]]) -> int:
    total = 0
    for bank in banks:
        n, start, joltage = len(bank), 0, 0
        for pos in range(12):
            max_search_end = n - (12 - pos - 1)
            max_digit = bank[start]
            max_idx = start
            for i in range(start, max_search_end):
                if bank[i] > max_digit:
                    max_digit = bank[i]
                    max_idx = i
            start = max_idx + 1
            joltage += max_digit * (10 ** (12 - pos - 1))
        total += joltage
    return total

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        banks = read_input("input_test.txt")
    else:
        banks = read_input("input.txt")
    result_pt1 = solve_pt1(banks)
    result_pt2 = solve_pt2(banks)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")