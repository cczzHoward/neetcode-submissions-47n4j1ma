class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        const res = [];

        const makeCombination = function (idx, comb, total) {
            if (total === target) {
                res.push([...comb]);
                return;
            }

            if (total > target || idx >= nums.length) {
                return;
            }

            comb.push(nums[idx]);
            makeCombination(idx, comb, total + nums[idx]);
            comb.pop();
            makeCombination(idx+1, comb, total);
        }
        
        makeCombination(0, [], 0);
        return res;
    }
}
