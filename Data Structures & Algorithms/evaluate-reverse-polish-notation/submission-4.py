class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for element in tokens:
            if element not in "+-*/":
                stack.append(int(element))
                continue
            
            n2 = stack.pop()
            n1 = stack.pop()

            if element == '+':
                stack.append(n1+n2)
            elif element == '-':
                stack.append(n1-n2)
            elif element == '*':
                stack.append(n1*n2)
            elif element == '/':
                stack.append(int(n1/n2))
        
        return stack.pop()