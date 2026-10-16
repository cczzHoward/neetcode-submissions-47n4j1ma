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
                if not stack: return False

                cur_want = valid_dict[element]
                stack_top = stack.pop()

                if cur_want != stack_top:
                    return False
        
        return not stack

