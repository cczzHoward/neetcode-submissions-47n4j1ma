class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. create dict {value: index}
        num_dict = defaultdict(int)

        # 2. for loop
        for i, num in enumerate(nums):    
            # 3. what number we need?
            need = target - num
            # 4. if we have the "need" number -> return
            if need in num_dict:
                return [num_dict[need], i]

            # 5. if not, add cur to dict
            num_dict[num] = i
        
        return False