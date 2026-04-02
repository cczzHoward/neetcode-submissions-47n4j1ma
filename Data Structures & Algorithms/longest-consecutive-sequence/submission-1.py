class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # 找到現在subsequence的最小值
            if (num-1) not in num_set:
                length = 1
                # 一個一個往後推，如果有連續出現的數字就讓 longest+1
                while(num+length in num_set):
                    length += 1
                longest = max(longest, length)
        
        return longest