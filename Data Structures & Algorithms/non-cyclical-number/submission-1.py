class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            output = 0
            while n:
                output += (n%10)**2
                n //= 10
            return output            
        
        visit = set()
        while n not in visit:
            visit.add(n)
            n = sumOfSquares(n)

            if n == 1:
                return True
        return False