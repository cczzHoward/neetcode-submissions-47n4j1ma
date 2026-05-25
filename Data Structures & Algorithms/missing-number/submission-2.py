class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        # 這個部分在做的事情就是
        # sum(0~n) - sum(實際有的數字) = 缺少的數字
        for i in range(len(nums)):
            # i 是期望有的數字
            # nums[i] 實際的數字
            res += (i - nums[i])
        
        return res