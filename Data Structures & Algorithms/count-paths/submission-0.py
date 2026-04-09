class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        # 最底下那一排全部都是一 所以不用跑
        # 從第二排開始跑就好 所以只要跑 m-1 徘 (m-1 次迴圈)
        for i in range(m-1):
            newRow = [1] * n
            # 最右邊的數字 (n-1) 一定是1
            # 所以從右邊數來第二個數字 (n-2) 開始跑
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        
        return row[0]