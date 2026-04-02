class Solution:
    def rob(self, nums: List[int]) -> int:
        # case1 如果我們搶第一間房子 -> 不能搶最後一間房子
        # case2 如果我們搶最後一間房子 -> 不能搶第一間房子
        # 從 case1 與 case2 找最大的 (拆成兩個 sub problem: House Robber I)
        # 有一個 edge case 是如果整排房子只有一間, 所以多一個 nums[0]
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    # 這個 function 就是 House Robber I 的解法
    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob

        return rob2
