class Solution:
    def checkValidString(self, s: str) -> bool:
        # 這題是 greedy
        # 有點不好理解, 可以在複習
        
        leftMin, leftMax = 0, 0

        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            
            # leftMax < 0 -> 不可能成功
            if leftMax < 0:
                return False
            # leftMin < 0 -> 還有機會成功 -> 要把 leftMin 歸零
            if leftMin < 0:
                leftMin = 0
        
        return leftMin == 0