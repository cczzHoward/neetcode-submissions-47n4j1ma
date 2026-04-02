class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def bt(n, substring, openN, closeN):
            if len(substring) == n*2:
                res.append(substring)
                return
            
            if openN < n:
                bt(n, substring+'(', openN+1, closeN)
            
            if closeN < openN:
                bt(n, substring+')', openN, closeN+1)

        res = []
        bt(n, "", 0, 0)
        return res
        