class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            # right height is shorter than left height -> right is the bottleneck of the water can be filled -> move right index
            if left_max > right_max:
                # move right index
                right -= 1
                # update right_max value
                right_max = max(right_max, height[right])
                # caculate how much water can be filled in this block and add to res variable
                res += right_max - height[right]
            # left height is shorter than right height -> left is the bottle neck of the water can be filled -> move left index
            else:
                # move left index
                left += 1
                # update left_max value
                left_max = max(left_max, height[left])
                # caculate how much water can be filled in this block and add to res variable
                res += left_max - height[left]
        
        return res