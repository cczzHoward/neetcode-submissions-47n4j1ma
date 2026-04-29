class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxHeap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # 有兩個石頭以上(含)就要碰撞
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # 第一顆石頭一定 >= 第二顆石頭
            if first < second:
                heapq.heappush(stones, first -second)        
        
        # 回傳前塞一個零
        # 原本 stones 是空的 => return 0
        # 原本 stones 有一值 => return value(因為 value 一定比 0 小)
        # stones.append(0)
        # return abs(stones[0])
        
        # 寫法可以在優化
        return abs(stones[0]) if stones else 0
