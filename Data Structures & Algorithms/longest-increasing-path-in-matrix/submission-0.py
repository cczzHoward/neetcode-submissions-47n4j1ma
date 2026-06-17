class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} # pair: (r, c) -> LIP

        def dfs(r, c, prevVal):
            # return case
            # outbound
            # 隔壁數字沒有比現在的數字大 (不符合標準)
            if (r<0 or r==ROWS or
                c<0 or c==COLS or
                matrix[r][c] <= prevVal):
                return 0
            
            # cache
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            # 往四個方向走走看
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
            dp[(r, c)] = res
            
            # 取最大值 return
            return res
        
        # 每一格都走走看, 被 cache 的不會重複計算
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        
        return max(dp.values())