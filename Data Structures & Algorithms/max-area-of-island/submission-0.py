class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # 紀錄已經遍歷過的座標
        visit = set()

        def dfs(r, c):
            # 不合法格子直接回傳 0, 判斷標準如下
            # r 是否 outbound
            # c 是否 outbound
            # 是否是海洋 (不是陸地)
            # 是否還沒已經被遍歷過
            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] == 0 or
                (r, c) in visit):
                return 0
            
            # 合法格子我們加入並往四個方向遍歷
            visit.add((r, c))
            return(1 + dfs(r + 1, c) +
                       dfs(r - 1, c) +
                       dfs(r, c + 1) +
                       dfs(r, c - 1))

        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area