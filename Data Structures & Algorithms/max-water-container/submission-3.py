class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        left, right = 0, len(heights)-1

        while left < right:
            height = min(heights[left], heights[right])
            largest = max(largest, (right-left)*height)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return largest