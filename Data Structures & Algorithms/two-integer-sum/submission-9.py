class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()

        for i, num in enumerate(nums):
            # 1. how much we need to get target
            need = target - num
            
            # 2. check if we have the needed number
            if need in num_dict:
                return [num_dict[need], i]

            # 3. add current number to num_dict
            num_dict[num] = i
        
        # 4. return False if we end loop
        return False