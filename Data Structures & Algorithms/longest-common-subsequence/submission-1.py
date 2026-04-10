class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 建立數字為 0 的 2D matrix
        # col => text2's length + 1
        # row => text1's legnth + 1
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        # 從最右下角開始 逐行跑每一個格子
        # 如果格子對到相同的字母 => 該格算是 1 個長度 加上 右下角的長度 (因為兩個字母都被用掉 所以要往右下角, 不能只往又或是只往下)
        # 沒對到相同字母 => 該格算是 0 個長度 加上 max(右邊的長度, 下面的長度) [因為可以選其中一個字串拿掉一個字母所以有兩個方向可以走]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else: 
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        # 2D matrix 全部填寫完後 => dp[0][0] 就會是答案
        return dp[0][0]