class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l, r = 0, 0
        max_length = 0

        while r < len(s):
            # 目前元素是否已經出現過
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            # 加入目前指標的元素
            char_set.add(s[r])
            r += 1
            max_length = max(max_length, r-l)
        
        return max_length