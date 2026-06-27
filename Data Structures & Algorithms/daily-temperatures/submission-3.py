class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 每格都是預設沒有比當日更熱的天氣(0)
        res = [0] * len(temperatures)
        stack = [] # pair: [temprature, index]

        for i, t in enumerate(temperatures):

            # 看現在在 iterate 的溫度有沒有比 stack 裡的高 => 有的話就可以更新紀錄 
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex 

            # 記得要把現在在 iterate 的溫度也加進 stack
            stack.append([t, i])
        
        return res