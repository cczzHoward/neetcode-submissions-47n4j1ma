class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left, right = 0, len(heights)-1

        while left < right:
            length = right-left
            height = min(heights[left], heights[right])
            res = max(res, length * height)

            # left height is shorter than right height -> left height is the bottleneck of filling water -> move left pointer
            if heights[left] < heights[right]:
                left += 1
            
            # right height is shorter than left height -> right height is the bottleneck of filling water -> move right pointer    
            else:
                right -= 1
        
        return res