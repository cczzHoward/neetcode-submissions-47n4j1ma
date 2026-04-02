class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # sub_set: 目前的 [] 狀況
        # pick: 是否被選過
        res = []

        def bt(nums, sub_set, pick):
            if len(sub_set) == len(nums):
                res.append(sub_set.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    sub_set.append(nums[i])
                    pick[i] = True
                    bt(nums, sub_set, pick)
                    sub_set.pop()
                    pick[i] = False
        
        bt(nums, [], [False] * len(nums))
        return res