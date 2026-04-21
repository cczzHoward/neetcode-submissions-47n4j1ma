class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        # 是否 visit 過的 block
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # 不合法格子直接 return
            # outbound
            # 已經走過(visited)了
            # 這格比上一格還要矮 (因為是從海洋反推陸地, 所以條件會反過來)
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                heights[r][c] < prevHeight):
                return
            
            # 合法的格子可以 visit
            visit.add((r, c))

            # 四個方向嘗試遍歷
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        # 從海洋開始延伸可以到達的 block => 存入 pac 或 atl
        # 再取 pac 與 atl 的交集

        # 上橫排下橫排
        for c in range(COLS):
            #上橫排
            dfs(0, c, pac, heights[0][c])
            #下橫排
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        # 左直排右直排
        for r in range(ROWS):
            # 左直排
            dfs(r, 0, pac, heights[r][0])
            # 右直排
            dfs(r, COLS-1, atl,heights[r][COLS-1])
        
        # 取交集
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
                    
