class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # 如果現在算的 nums[i] 跟前一個 nums[i-1] 是依樣的數字就跳過，避免重複計算
            if (i>0 and nums[i] == nums[i-1]):
                continue

            l = i+1
            r = len(nums)-1

            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # 手動把 l 往右邊移一格，不然會無限迴圈
                    l += 1
                    # l 要移動到跟前面push進去的 nums[l] 不一樣的數字，不然會重複計算一樣的case
                    while (nums[l] == nums[l-1] and l<r):
                        l += 1
            
        return res


        