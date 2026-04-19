class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addGrid(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                grid[r][c] == -1):
                return
            
            q.append([r, c])
            visit.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c)) # 忘記這一行了, 要記得 append queue 同時要記錄到 visit 裡面

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addGrid(r+1, c)
                addGrid(r-1, c)
                addGrid(r, c+1)
                addGrid(r, c-1)
            
            dist += 1
