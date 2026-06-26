class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0

        mapping = {'(':')', '[':']', '{':'}'}
        
        while i < len(s):
            if s[i] in "{[(":
                stack.append(s[i])
            else:
                if not stack or mapping[stack.pop()] != s[i]:
                    return False

            i += 1
                

            
        
        # stack 要是空的(全部都處理完畢了)才會是 True
        return not stack