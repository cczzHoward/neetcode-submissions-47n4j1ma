class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 這題畫 decision tree 對理解很有幫助！
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2 (skip 1 day)

        dp = {} # key=(i, canBuy) val=max_profit

        def dfs(i, canBuy):
            # out of bound
            if i >= len(prices):
                return 0
            
            # caching
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            
            # Buy
            if canBuy:
                buy = dfs(i+1, not canBuy) - prices[i]
                cooldown = dfs(i+1, canBuy)
                dp[(i, canBuy)] = max(buy, cooldown)
            
            # Sell
            else:
                buy = dfs(i+2, not canBuy) + prices[i]
                cooldown = dfs(i+1, canBuy)
                dp[(i, canBuy)] = max(buy, cooldown)
            
            return dp[(i, canBuy)]
        
        return dfs(0, True)

            