class CountSquares:

    def __init__(self):
        # ptsCount: point -> count
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.pts:
            # 沒有正方形的對角點 or 沒有其中一個邊 -> continue
            if (abs(px-x) != abs(py-y)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res
