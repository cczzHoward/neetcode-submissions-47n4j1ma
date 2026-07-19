class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair: [temperature, index]
        res = [0] * len(temperatures)

        for i, tem in enumerate(temperatures):

            # update res if we find avalible element
            while stack and tem > stack[-1][0]:
                stack_tem, stack_i = stack.pop()
                res[stack_i] = i-stack_i
            
            # append current temperature in stack
            stack.append([tem, i])

        return res