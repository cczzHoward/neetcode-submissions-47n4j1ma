class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let obj = {};

        for (let i = 0; i < nums.length; i++) {
            if (obj[nums[i]]) {
                return true
            }
            obj[nums[i]] = 1;
        } 
        return false;
    }
}
