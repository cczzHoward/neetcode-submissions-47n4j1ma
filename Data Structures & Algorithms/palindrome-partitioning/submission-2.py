class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # 沒有字可以找代表目前的 part 是該被 return 的
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                # 如果是 palindrome 就把這個 palindrom 加進 part
                # index i~j 是 palindrome
                if self.isPal(s, i, j):
                    part.append(s[i:j+1])
                    # 從下一個字母開始繼續往下找 (j+1 開始)
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res
    
    def isPal(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False    
            l += 1
            r -= 1
        return True
        
        



        

