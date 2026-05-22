class Solution:
    def hammingWeight(self, n: int) -> int:
        # solution 2
        res = 0
        while n:
            # 透過 and 運算數 1 有幾個
            n = n & (n-1)
            res += 1
        return res