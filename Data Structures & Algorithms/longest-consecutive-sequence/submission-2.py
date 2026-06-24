class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            # 確認這個數字是這個 subsequence 裡面最小的再開始跑
            if (num-1) not in num_set:
                length = 1
                while (num+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest