class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def bt(ind):
            if ind >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[ind])
            bt(ind+1)
            subset.pop()

            while ind+1 < len(nums) and nums[ind] == nums[ind+1]:
                ind += 1
            bt(ind+1)

        res = []
        subset = []
        nums.sort()
        bt(0)

        return res

        