class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 達到標準的 index
        good = set()

        for t in triplets:
            # 如果有大於 target 的 element => 直接跳過
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # 紀錄可以達到 target element 的數量
            for ind, value in enumerate(t):
                if value == target[ind]:
                    good.add(ind)
        
        # 是否達到預期 (三個 element 都要達到才 return True)
        return len(good) == 3