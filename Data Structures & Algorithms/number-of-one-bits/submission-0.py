class Solution:
    def hammingWeight(self, n: int) -> int:
        # solution 1
        res = 0
        while n:
            # 如果尾巴是1就會加1
            res += n % 2
            # 把整個數字往右邊推一位數
            # ex: 1001100 -> 100110
            n = n >> 1
        return res