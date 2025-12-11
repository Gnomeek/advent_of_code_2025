import heapq
import sys

class UF(object):
    def __init__(self, size: int):
        self.size = size
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.is_all_connected = False


    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x


    def union(self, x: int, y: int) -> bool:
        a, b = self.find(x), self.find(y)
        if a == b:
            return False
        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
            self.rank[a] += self.rank[b]
        else:
            self.parent[a] = b
            self.rank[b] += self.rank[a]
        if self.rank[a] == self.size or self.rank[b] == self.size:
            self.is_all_connected = True
        return True
    

    def get_group_size(self) -> dict[int, int]:
        group_size = {}
        for i in range(self.size):
            root = self.find(i)
            if root not in group_size:
                group_size[root] = self.rank[root]
        return group_size
    

    def __repr__(self):
        return f"parent: {self.parent}, rank: {self.rank}"
    

    def __str__(self):
        return f"parent: {self.parent}, rank: {self.rank}"
    

class Dot(object):
    x: int = 0
    y: int = 0
    z: int = 0

    def __init__(self, x: str, y: str, z: str):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)


    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


    def distance(self, another: 'Dot'):
        return (self.x - another.x) ** 2 + (self.y - another.y) ** 2 + (self.z - another.z) ** 2


def read_input(file_path: str) -> list[Dot]:
    dots = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            x, y, z = line.strip().split(",")
            dots.append(Dot(x, y, z))
    return dots


def solve_pt1(dots: list[Dot], steps: int, topn: int) -> int:
    n = len(dots)
    uf, heap = UF(n), []
    for i in range(n):
        for j in range(i+1, n):
            a, b = dots[i], dots[j]
            heapq.heappush(heap, (a.distance(b), i, j))
    while steps > 0:
        _, i, j = heapq.heappop(heap)
        uf.union(i, j)
        steps -= 1
    res = 1
    sizes = sorted(set(uf.get_group_size().values()), key=lambda x:-x)
    sizes = sizes[:topn] if topn != 0 else sizes
    for i in sizes:
        res *= i
    return res


def solve_pt2(dots: list[Dot]) -> int:
    n = len(dots)
    uf, heap = UF(n), []
    for i in range(n):
        for j in range(i+1, n):
            a, b = dots[i], dots[j]
            heapq.heappush(heap, (a.distance(b), i, j))
    while len(heap) > 0:
        _, i, j = heapq.heappop(heap)
        uf.union(i, j)
        if uf.is_all_connected:
            return dots[i].x * dots[j].x


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        dots, steps, topn = read_input("input_test.txt"), 10, 0
    else:
        dots, steps, topn = read_input("input.txt"), 1000, 3
    result_pt1 = solve_pt1(dots, steps, topn)
    result_pt2 = solve_pt2(dots)
    print(f"Part 1: {result_pt1}")
    print(f"Part 2: {result_pt2}")