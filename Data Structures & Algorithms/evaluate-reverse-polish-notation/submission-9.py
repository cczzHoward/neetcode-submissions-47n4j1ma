class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # oprator
            if token in '+-*/':
                # get value
                v2 = int(stack.pop())
                v1 = int(stack.pop())

                # calculate
                if token == '+':
                    result = v1 + v2
                elif token == '-':
                    result = v1 - v2
                elif token == '*':
                    result = v1 * v2
                else:
                    result = int(v1 / v2)
                
                stack.append(result)

            # number
            else:
                stack.append(int(token))
        
        return stack[0]
