class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            # 因為左側最高的陸地比較矮 -> 左側才是裝水的 bottleneck
            if leftMax < rightMax:
                # 移動左側 index
                left += 1
                # 更新現在左側最高的陸地
                leftMax = max(leftMax, height[left])
                # 可以裝到的水位(leftMax) - 陸地的高度(height[left]) => 實際上這一個格子有的水位
                res += leftMax - height[left]
            # 因為右側最高的陸地比較矮 -> 右側才是裝水地 bottlenect
            else:
                # 移動右側 index
                right -= 1
                # 更新現在右側最高的陸地
                rightMax = max(rightMax, height[right])
                # 可以裝到的水位(rightMax) - 陸地的高度(height[right]) => 實際上這一個格子有的水位
                res += rightMax - height[right]
        
        # 把所有水位加入 res 並 return
        return res