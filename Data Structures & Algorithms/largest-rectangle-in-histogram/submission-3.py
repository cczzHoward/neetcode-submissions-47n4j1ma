class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stack_index, stack_height = stack.pop()
                max_area = max(max_area, stack_height * (i - stack_index))
                start = stack_index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights)-i))
        
        return max_area

                