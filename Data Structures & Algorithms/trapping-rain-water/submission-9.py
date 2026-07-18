class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            # left bottleneck of filling water -> move left
            if left_max < right_max:
                # move pointer
                left += 1
                # update left_max
                left_max = max(left_max, height[left])
                # caculate water of this index
                res += left_max - height[left]      
                           
            # right bottleneck of filling water -> move right
            else:
                # move pointer
                right -= 1
                # update right_max
                right_max = max(right_max, height[right])
                # cacluate water of this index
                res += right_max - height[right]
        
        return res