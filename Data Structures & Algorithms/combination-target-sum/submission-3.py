class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def bt(i, sub_sum):
            if sub_sum == target:
                res.append(subset.copy())
                return
            if sub_sum >= target or i >= len(nums):
                return
            
            subset.append(nums[i])
            bt(i, sub_sum + nums[i])

            subset.pop()
            bt(i+1, sub_sum)
            

        bt(0, 0)
        return res