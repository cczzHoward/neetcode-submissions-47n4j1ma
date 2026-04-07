class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp => [0 ... amount]
        # amount + 1 是因為有多一個 "0"

        dp = [amount+1] * (amount+1)
        # 0 元可以用 0 個硬幣達成
        dp[0] = 0
        
        # 每一輪都填寫 dp[a]
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # example a=7, c=4
                    # dp[7] = min(dp[7], 1 + dp[3])
                    #                    1個四元 + 達成三元的硬幣數
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[amount] if dp[amount] != amount+1 else -1