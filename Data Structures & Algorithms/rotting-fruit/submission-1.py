class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        def addOrange(r, c):
            # 要改外部變數要宣告
            nonlocal fresh
            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] != 1):
                return
            
            grid[r][c] = 2
            q.append([r, c])
            fresh -= 1

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                addOrange(r+1, c)
                addOrange(r-1, c)
                addOrange(r, c+1)
                addOrange(r, c-1)
            
            time += 1

        return time if fresh == 0 else -1