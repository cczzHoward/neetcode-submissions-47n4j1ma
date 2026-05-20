class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford algorithm
        prices = [float("inf")] * n
        prices[src] = 0
        
        # 用類似 BFS 的方式來解決這個問題
        # 最多可以轉乘 K 次所以我們可以走 edge K+1 次
        for i in range(k+1):
            tmpPrices = prices.copy()

            # s=source, d=destination, p=price
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]