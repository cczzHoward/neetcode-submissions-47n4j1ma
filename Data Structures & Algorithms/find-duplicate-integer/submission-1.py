class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. 把array看成linked list, index看為值 value看為指針
        # 2. Floyd's 演算法

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