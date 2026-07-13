class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {} # pair: value -> index

        for i, num in enumerate(nums):
            diff = target - num

            if diff in num_dict:
                return [num_dict[diff], i]    

            num_dict[num] = i
            