class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for element in tokens:
                if element == '+':
                    stack.append(stack.pop()+stack.pop())
                elif element == '-':
                    n2 = stack.pop()
                    n1 = stack.pop()
                    stack.append(n1-n2)
                elif element == '*':
                    stack.append(stack.pop()*stack.pop())
                elif element == '/':
                    n2 = stack.pop()
                    n1 = stack.pop()
                    stack.append(int(n1/n2))
                else:
                    stack.append(int(element))

        return stack.pop()
