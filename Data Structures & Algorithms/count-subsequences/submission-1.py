class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 這題大概理解 7~8 成, pointer 的移動還有些問題 => need review
        # 我發現 base case 兩個順序不能交換, 這是為甚麼?? ( 理解降到 5~6 成了:( )
        cache = {}

        # i: index of s
        # j: index of t
        def dfs(i, j):
            # base case
            # string t is ""(empty)
            if j == len(t):
                return 1
            # string s is ""(empty)
            if i == len(s):
                return 0

            # cache
            if (i, j) in cache:
                return cache[(i, j)]
            
            #   如果這個字母一樣
            # ->我們可以兩個字串 pointer 都往下移動, 或是一個移動一個不移動
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
            # 如果不一樣移動一個 pointer 即可
            else:
                cache[(i, j)] = dfs(i+1, j)
            
            return cache[(i, j)]
        return dfs(0, 0)
