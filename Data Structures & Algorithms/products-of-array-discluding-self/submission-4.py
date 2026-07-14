class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums   : [ 1,  2,  3,  4]
        prefix : [ 1,  2,  6, 24]
        postfix: [24, 24, 12,  4]

        res    : [24, 12,  8,  6]
        res[1] = prefix[0]   * postfix[2]
        res[2] = prefix[1]   * postfix[3]
        res[i] = prefix[i-1] * postfix[i+1]

        
        prefix : [           1,                    2,                    6,          24]
        postfix: [          24,                   24,                   12,           4]
        res    : [1*postfix[1], prefix[0]*postfix[2], prefix[1]*postfix[3], prefix[2]*1]
        res    : [          24,                   12,                    8,           6]
        
        兩個迴圈, 一個在 res 放 prefix, 一個在 res 放 postfix, 然後相乘載一起 return
        """

        res = [1] * len(nums)
        # 先放 prefix
        prefix = 1
        for i in range(len(nums)-1):
            prefix *= nums[i]
            res[i+1] *= prefix
        
        # 再放 postfix
        postfix = 1
        for i in range(len(nums)-1, 0, -1):
            postfix *= nums[i]
            res[i-1] *= postfix
        
        return res