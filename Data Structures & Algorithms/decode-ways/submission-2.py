class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        for i in range(len(s)-1, -1, -1):
            # 沒有 decode 方法可以從 0 開始
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
        
            # 如果有兩個數字可用 and 
            # 第一個數字為 1 or 
            # (第一個數字為 2 and 第二個數字為 0~6)
            if (i+1 < len(s) and (s[i] == "1" or 
                s[i] == "2" and s[i+1] in "0123456")):
                # 可以變成 dp[i] = dp[i+1] + dp[i+2]
                # 上面加過 dp[i+1] 了所以這邊只加 dp[i+2]
                dp[i] += dp[i+2]
        return dp[0]
    
        
        