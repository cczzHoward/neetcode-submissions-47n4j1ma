class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = defaultdict(int)
        
        for num in nums:
            if num in nums_dict:
                return True
            nums_dict[num] += 1
        return False