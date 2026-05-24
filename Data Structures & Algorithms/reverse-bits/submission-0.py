class Solution:
    def reverseBits(self, n: int) -> int:
        # 這一題沒有到很理解
        # 要複習 + 要學習 << >> 這兩個運算子
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))

        return res