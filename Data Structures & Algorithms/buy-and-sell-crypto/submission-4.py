class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while (r<len(prices)):
            print(l,r)
            if (prices[l]>prices[r]):
                l = r
            elif (prices[r]-prices[l] > profit):
                profit = prices[r]-prices[l]
            r += 1
        return profit