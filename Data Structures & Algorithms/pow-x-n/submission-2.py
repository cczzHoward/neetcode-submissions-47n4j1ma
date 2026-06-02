class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 這題有一點點小矇, 不太懂 recursion 怎麼跑的, 要多複習
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x, n//2)
            res = res * res
            # 處理基數 n & 偶數 n
            return x*res if n%2 else res
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res