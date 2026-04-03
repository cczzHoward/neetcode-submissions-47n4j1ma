class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            # odd length
            l, r = i, i
            # l, r 在合法範圍 and 左右字元相等
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 是最長的就換掉 res
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                
                # 往外擴展
                l -= 1
                r += 1

            # even length
            l, r = i, i+1
            # l, r 在合法範圍 and 左右字元相等
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 是最長的就換掉 res
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                
                # 往外擴展
                l -= 1
                r += 1
        
        return res
