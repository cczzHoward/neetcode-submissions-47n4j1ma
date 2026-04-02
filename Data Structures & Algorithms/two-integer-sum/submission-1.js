class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        nums = nums.map((num, index) => ({num, index})).sort((a, b) => (a.num-b.num));
        let left = 0;
        let right = nums.length-1;
        while (left < right) {
            let sum =  nums[left].num + nums[right].num;
            if (sum === target) {
                return ([nums[left].index, nums[right].index]);
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return ;
    }
}
