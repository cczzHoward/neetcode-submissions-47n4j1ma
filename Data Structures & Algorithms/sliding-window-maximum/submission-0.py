class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_num = -float("infinity")
        num_dict = {}
        res = []

        for i in range(k):
            num_dict[nums[i]] = 1 + num_dict.get(nums[i], 0)
        res.append(max(num_dict))

        left, right = 0, k
        while right < len(nums):
            num_dict[nums[right]] = 1 + num_dict.get(nums[right], 0)
            right += 1
            num_dict[nums[left]] -= 1
            if num_dict[nums[left]] == 0:
                del num_dict[nums[left]]
            left += 1
            res.append(max(num_dict))

        return res
        