class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for element in s:
            # 右括弧的情況
            if element in mapping:
                # 檢查stack是否為空(否的話給一個'#'以免報錯)
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '#'

                if mapping[element] != top_element:
                    return False
            # 左括弧的情況
            else:
                stack.append(element)
            
        return not stack