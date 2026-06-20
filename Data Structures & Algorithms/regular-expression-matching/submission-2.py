class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # TOP-Down Memorization -> improve with cache

        cache = {}

        # i -> s index
        # j -> p index
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
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
                cache[(i, j)] = (dfs(i, j+2) or          # don't use *
                                (match and dfs(i+1, j)))  # use *
                return cache[(i, j)]

            # simple match case (s[i] == p[j])
            if match:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]
            
            # no match
            cache[(i, j)] = False
            return cache[(i, j)]
        
        return dfs(0, 0)




