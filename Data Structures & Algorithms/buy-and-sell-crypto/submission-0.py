class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0;
        index = 1;
        while(index<len(prices)):
            if (prices[index] < buy):
                buy = prices[index]
            elif (prices[index]-buy > profit):
                profit = prices[index]-buy
            index += 1
        return profit
        