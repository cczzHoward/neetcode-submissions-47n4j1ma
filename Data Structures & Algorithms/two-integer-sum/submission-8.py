class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # pair: number -> index
        num_dict = {}

        for i, num in enumerate(nums):
            # 差多少 (diff) 可以達到 target
            diff = target - num
            # 檢查 diff already iterate? -> return combination if yes
            if diff in num_dict:
                return [num_dict[diff], i]
            
            # 把現在這個值加入 num_dict
            num_dict[num] = i
        