class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        # r pointer 還沒有到達 list 的尾巴
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            
            # l, r 是這個步驟可以走到的 partion
            l = r + 1
            r = farthest

            # 加一步驟
            res += 1
        
        return res