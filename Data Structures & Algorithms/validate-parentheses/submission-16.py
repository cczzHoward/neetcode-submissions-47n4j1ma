class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {')':'(', ']':'[', '}':'{'}
        stack = []

        for element in s:
            # case ([{
            if element in "([{":
                stack.append(element)

            # case }])
            else:
                if stack:
                    stack_top = stack.pop()
                else:
                    stack_top = '#'
                
                if stack_top != valid_dict[element]:
                    return False
        
        return not stack

