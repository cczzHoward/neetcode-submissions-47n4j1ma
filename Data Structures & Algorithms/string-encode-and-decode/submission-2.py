class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # 找到這個字串的長度('#'前的數字)
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # 透過字串長度可以找到 s[i:j] 就是我們要找的字串
            i = j+1
            j = i+length
            res.append(s[i:j])

            # 加入後往下一個字串移動
            i = j

        return res
