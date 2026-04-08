class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 如果 sum(nums) / 2 是基數 => 不可能可以分成兩個一樣的 subset
        if sum(nums) % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            # 如果沒有 nextDP 會跑無限迴圈, 因為迴圈還沒跑完就在 dp 後面加東西
            # 應該跑完後一次全部加進 dp 裡面
            nextDP = set()
            
            # 讓每一個目前 dp 裡面的數字加上現在 iterate 到的數字
            # 如果 iterate 到的數字 + dp 裡的數字 == target, 可以直接回傳 True
            for t in dp:
                if (t+nums[i]) == target:
                    return True
                nextDP.add(t)
                nextDP.add(t+nums[i])
            dp = nextDP
        
        return False
        