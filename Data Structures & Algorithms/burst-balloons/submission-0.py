class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        # cache pair: subsequence(l, r) -> result
        dp = {}

        def dfs(l, r):
            # outbound (沒有氣球需要處理了)
            if l > r:
                return 0
            # cache
            if (l, r) in dp:
                return dp[(l, r)]
            
            # 開始計算 (l, r) 的值 (default by 0)
            dp[(l, r)] = 0
            for i in range(l, r+1):
                # dynamic programming
                # 不懂要去複習影片 (細節太複雜不知道怎麼放 comment)
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        # 放第二個數字
        return dfs(1, len(nums)-2)
