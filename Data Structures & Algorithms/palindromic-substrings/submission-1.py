class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(s, l, r):
            res = 0
            # l and r are both inbound & they are both same char
            # 往外擴張找下一組
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # 回傳由這個 s 為中心的所有 palindrome 的數量
            return res
        
        res = 0
        for i in range(len(s)):
            # odd length
            res += helper(s, i, i)

            # even length
            res += helper(s, i, i+1)
        return res
