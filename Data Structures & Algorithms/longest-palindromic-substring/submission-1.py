class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            nonlocal res, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                
                l -= 1
                r += 1

        res = ""
        resLen = 0

        # 從中心往外擴張找最常 palindrome
        for i in range(len(s)):
            
            # odd length
            helper(i, i)
            
            # even length
            helper(i, i+1)
        
        return res
