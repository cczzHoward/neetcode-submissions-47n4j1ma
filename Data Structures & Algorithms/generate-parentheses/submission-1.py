class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def bt(res, n, stack='', openN=0, closeN=0):
            if len(stack) == n*2:
                res.append(stack)
                return
            
            if openN < n:
                bt(res, n, stack+'(', openN+1, closeN)
            
            if closeN < openN:
                bt(res, n, stack+')', openN, closeN+1)

        res = []
        bt(res, n)
        return res