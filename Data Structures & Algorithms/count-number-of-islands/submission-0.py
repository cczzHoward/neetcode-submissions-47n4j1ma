class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            # 從進入 bfs 的那一格開始放
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            # 開始跑 queue 中的 element 直到 queue 空掉
            while q:
                row, col = q.popleft()
                # 分別對應四個方向: 右, 左, 下, 上
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    # 計算鄰近格子的座標
                    r, c = row + dr, col + dc

                    # 在邊界內 & 是陸地('1') & 還未被訪問過
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands