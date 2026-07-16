class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case
        if not height: return 0

        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        res = 0

        while left < right:
            # left land is shorter than right land -> left land is the bottleneck of filling water -> move left index
            if left_max < right_max:
                # move left index
                left += 1
                # update max height of left land
                left_max = max(left_max, height[left])
                # add the number to res that water can be fill in this block
                res += left_max - height[left]

            # right land is shorter than left land -> right land is the bottleneck of filling water -> move right index
            else:
                # move right index
                right -= 1
                # update max height of right land
                right_max = max(right_max, height[right])
                # add the number to res that water can be fill in this block
                res += right_max - height[right]
        
        return res