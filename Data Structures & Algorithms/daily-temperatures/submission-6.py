class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair:[i, tem]
        result = [0] * len(temperatures)

        for i, tem in enumerate(temperatures):
            
            # if cur temp higher than top stack?
            while stack and tem > stack[-1][1]:
                cur_i, cur_tem = stack.pop()
                result[cur_i] = i - cur_i

            stack.append([i, tem])
        
        return result