class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0 # l:buy, r:sell
        max_profit = 0

        while (r < len(prices)) :
            # 是否營利？
            # 有:看是否是max_profit
            # 否：把buy指針移到sell指針上成為新的buy指針
            if (prices[l] < prices[r]):
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return max_profit
                
            