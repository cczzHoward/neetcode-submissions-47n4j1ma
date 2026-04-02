class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 建立對照表：右括號找左括號
        mapping = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in mapping:
                # 這是右括號的情況
                # 1. 檢查 stack 是否為空 (若空則給一個假的值 '#' 避免報錯)
                # 2. 檢查 stack 頂端是否等於對應的左括號
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '#'
                
                if mapping[char] != top_element:
                    return False
            else:
                # 這是左括號的情況，推入堆疊
                stack.append(char)
                
        return not stack