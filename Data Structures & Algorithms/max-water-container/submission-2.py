class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maximum = 0

        while left < right:
            height = min(heights[left], heights[right])
            amount = height * (right-left)
            maximum = max(maximum, amount)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maximum