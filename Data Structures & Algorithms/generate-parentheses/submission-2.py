class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def bt(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                bt(openN+1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(')')
                bt(openN, closeN+1)
                stack.pop()

        res = []
        stack = []
        bt(0,0)
        return res