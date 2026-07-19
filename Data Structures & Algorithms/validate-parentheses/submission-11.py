class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {'}':'{', ']':'[', ')':'('}
        stack = []

        for string in s:
            # case )]}
            if string in valid_dict:
                if stack:
                    cur_element = stack.pop()
                else:
                    cur_element = '#'
                
                if cur_element != valid_dict[string]:
                    return False

            # case ([{
            else:
                stack.append(string)
        
        return not stack