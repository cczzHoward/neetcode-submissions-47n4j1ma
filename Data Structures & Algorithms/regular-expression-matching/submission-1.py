class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # i -> s index
        # j -> p index
        def dfs(i, j):
            # both index outbound -> perfect match
            if i >= len(s) and j >= len(p):
                return True
            # only j outbound -> something s wasn't be match -> False
            if j >= len(p):
                return False

            # i inbound and s[i], p[j] match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            # handle * case
            if (j+1) < len(p) and p[j+1] == '*':
                return (dfs(i, j+2) or          # don't use *
                        (match and dfs(i+1, j)))  # use *

            # simple match case (s[i] == p[j])
            if match:
                return dfs(i+1, j+1)
            
            # no match
            return False
        
        return dfs(0, 0)




