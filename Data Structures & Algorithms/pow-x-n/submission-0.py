class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = 1
        if n > 0:
            for i in range(n):
                res *= x
        else:
            for i in range(-n):
                res /= x
        
        return res