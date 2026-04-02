class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, n):
            if n == len(word):
                return True
            
            # 如果不符合條件就回傳 False
            # 1. 超出 list
            # 2. 不是我們要找的字
            # 3. 重複使用已使用的格子
            if (r < 0 or c >= COLS or
                c < 0 or r >= ROWS or
                board[r][c] != word[n] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r+1, c, n+1) or
                   dfs(r-1, c, n+1) or 
                   dfs(r, c+1, n+1) or 
                   dfs(r, c-1, n+1))
            path.remove((r, c))

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False
