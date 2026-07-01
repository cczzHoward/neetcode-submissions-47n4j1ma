class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. regard arrays as linked-list, index is value and value is pointer
        # 2. Floyd's algorithm
        
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow