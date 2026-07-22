class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [temperature, index]
        res = [0] * len(temperatures)

        for i, tem in enumerate(temperatures):
            
            while stack and tem > stack[-1][0]:
                stack_tem, stack_i = stack.pop()
                res[stack_i] = i-stack_i

            stack.append([tem, i])
        
        return res