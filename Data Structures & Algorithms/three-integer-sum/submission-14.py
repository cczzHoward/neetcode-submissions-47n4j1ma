class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for first_num in range(len(nums)):
            # skip this loop if we have already choose current number for first_num
            if first_num > 0 and nums[first_num] == nums[first_num-1]: continue

            # set left, right variable
            left, right = first_num+1, len(nums)-1

            while left < right:
                # total sum
                total = nums[left] + nums[right] + nums[first_num]
                
                # too big
                if total > 0:
                    right -= 1
                # too small
                elif total < 0:
                    left += 1
                # valid answer
                else:
                    # add result to res
                    res.append([nums[left], nums[right], nums[first_num]])

                    # update index
                    left += 1

                    # skip this loop if we have already choose current number for left index
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        
        return res