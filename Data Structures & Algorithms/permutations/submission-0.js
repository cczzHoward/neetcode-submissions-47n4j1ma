class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    constructor() {
        this.res = [];
    }


    permute(nums) {
        this.backtrack(nums, 0);
        return this.res;
    }

    backtrack(nums, idx) {
        if (idx === nums.length) {
            this.res.push([...nums]);
            return;
        }

        for (let i = idx; i < nums.length; i++) {
            [nums[idx], nums[i]] = [nums[i], nums[idx]];
            this.backtrack(nums, idx+1);
            [nums[idx], nums[i]] = [nums[i], nums[idx]];
        }
    }
}
