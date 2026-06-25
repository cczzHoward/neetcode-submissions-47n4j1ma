class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            # 檢查 s[left], s[right] 字元合法性
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            # update index
            left += 1
            right -= 1
        
        return True