class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0 # l:buy, r:sell
        max_profit = 0

        while (r < len(prices)):
            if (prices[l] < prices[r]):
                max_profit = max(max_profit, prices[r]-prices[l])
            else:
                # prices[r] is a better buy place than prices[l]
                l = r
            r += 1
        
        return max_profit