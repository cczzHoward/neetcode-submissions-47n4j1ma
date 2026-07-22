class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for element in tokens:
            if element not in "+-*/":
                stack.append(int(element))
                continue
            
            v2 = stack.pop()
            v1 = stack.pop()

            if element == '+':
                stack.append(v1+v2)
            elif element == '-':
                stack.append(v1-v2)
            elif element == '*':
                stack.append(v1*v2)
            elif element == '/':
                stack.append(int(v1/v2))
        
        return stack.pop()