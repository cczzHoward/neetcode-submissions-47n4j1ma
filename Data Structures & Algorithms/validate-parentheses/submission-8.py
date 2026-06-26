class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}

        for element in s:
            # 右括弧
            if element in ")]}":
                if stack:
                    cur_element = stack.pop()
                else:
                    cur_element = '#'
                
                if mapping[element] != cur_element:
                    return False

            # 左括弧
            else:
                stack.append(element)

        return not stack