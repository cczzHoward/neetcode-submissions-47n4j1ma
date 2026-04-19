class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        
        def addGrid(r, c):
            # 不合法 => return
            # r, c outbound
            # (r, c) visited
            # 這格是海洋 (無法通過)
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                grid[r][c] == -1):
                return
            
            # 合法就加入 queue
            visit.add((r, c))
            q.append([r, c])
        
        # 找出所有寶藏
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        # 對所有寶藏進行 bfs
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                # 把四個方向的 block 加進下一次的 bfs 排隊
                addGrid(r+1, c)
                addGrid(r-1, c)
                addGrid(r, c+1)
                addGrid(r, c-1)
            
            # 每輪 bfs 距離 +1 
            dist += 1
        