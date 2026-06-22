class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        appears = set()

        for num in nums:
            if num in appears:
                return True
            appears.add(num)
        return False