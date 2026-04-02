class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 解法
        # 透過 bt 每一 row 放一個 Q
        # 檢查 col 是否重複, pos_diag 是否重複, neg_diag 是否重複 (因為透過 bt 處理 row 所以不用檢查 row 是否重複)
        # 若重複就跳過, 沒有重複就可以放一個 Q 並往下一個 row 移動 (使用 bt)

        res = []
        board = [['.'] * n for i in range(n)]

        col = set()
        pos_diag = set() # (r + c) => constant
        neg_diag = set() # (r - c) => constant

        def bt(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = 'Q'

                bt(r+1)

                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = '.'
        
        bt(0)
        return res
