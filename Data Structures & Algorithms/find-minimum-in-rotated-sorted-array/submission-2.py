class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])
            # mid 在左邊的 subarray
            if nums[mid] >= nums[left]:
                left = mid + 1
            # mid 在右邊的 subarray
            else:
                right = mid - 1

        return res