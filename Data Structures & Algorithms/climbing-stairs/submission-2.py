class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1

        for i in range(n-1):
            temp = first + second
            first = second
            second = temp
        
        return second