class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for element in s:
            if element == '(' or element == '[' or element == '{':
                stack.append(element)
            else:
                # 如果 stack 為空直接 False
                if not stack:
                    return False
                
                if (element == ')' and stack[-1] != '(' 
                or element == ']' and stack[-1] != '[' 
                or element == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
            
        return not len(stack) #len() 可以省略