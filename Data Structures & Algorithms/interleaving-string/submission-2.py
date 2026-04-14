class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Solution1: dfs
        if len(s1) + len(s2) != len(s3):
            return False
            
        # cache
        dp = {}

        # i => s1 ind
        # j => s2 ind
        # k => s3 ind
        # k = i + j
        # 沒有多存一個 k 變數, 用計算的而已
        def dfs(i, j):
            # i, j out of bound => 遍歷s1, s2完畢 => True
            if i == len(s1) and j == len(s2):
                return True

            # cache
            if (i, j) in dp:
                return dp[(i, j)]

            # s1 目前 ind 是否與 s3 目前 ind 相等
            #                                       若相等則把 i 往後移動一格 (k 因為等於 i+j 所以也會被往後移動一格)
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            # s2 目前 ind 是否與 s3 目前 ind 相等
            #                                       若相等則把 j 往後移動一格 (k 因為等於 i+j 所以也會被往後移動一格)            # s2
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True
            
            # 都沒有找到代表是 False
            # 回傳前先記錄 cache
            dp[(i, j)] = False
            return False

        return dfs(0, 0)