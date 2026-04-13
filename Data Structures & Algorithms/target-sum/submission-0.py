class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 這題也很難
        # 之後應該要多做幾次多看幾次影片
        dp = defaultdict(int)

        dp[0] = 1 # (0 sum) -> 1 way
                  # 1 way to sum to zeror with first 0 elements
        
        for i in range(len(nums)):
            next_dp = defaultdict(int)

            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp

        return dp[target]