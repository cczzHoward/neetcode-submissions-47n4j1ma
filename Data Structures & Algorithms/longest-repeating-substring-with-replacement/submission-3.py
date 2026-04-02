class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r] ,0)
            max_freq = max(max_freq, count[s[r]])

            # 字串長度 - 最多字母的字數 > 可以代換的數字 => 無法成為一樣字母連續的字串
            while (r-l+1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res