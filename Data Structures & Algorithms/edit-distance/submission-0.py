class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]
        
        # initialize base case
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # bottom-up soloution
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                # 如果相等就代表直接往下一個字母前進
                if word1[i] == word2[j]:
                    cache[i ][j] = cache[i+1][j+1]
                # 不一樣的話有三條路: insert[i+1][j], remove[i][j+1], replace[i+1][j+1]
                # 所以會變成: 1(做一個操作本身視為1個 operation) + 三條路最少 operation 的那條路
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
            
        return cache[0][0]