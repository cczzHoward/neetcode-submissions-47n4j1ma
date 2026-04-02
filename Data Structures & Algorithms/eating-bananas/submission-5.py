class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/mid)

            # 如果在時間內成功吃完就可以更新紀錄 => 嘗試找更慢的速度             
            if hours <= h:
                res = mid
                right = mid - 1
            
            if hours > h:
                left = mid + 1

        return res