class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # 每一筆資料為 [溫度, 溫度的index]

        for i, t in enumerate(temperatures):
            # 如果現在這個溫度比 stack 裡面的大
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i-stackInd
            
            # 將這個溫度資料加進 stack
            stack.append([t, i])
            
        return res