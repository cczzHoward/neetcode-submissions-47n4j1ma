class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums) {
        function backtracking(ind) {
            if (ind === nums.length) {
                res.push([...subset]);
                return;
            }

            subset.push(nums[ind]);
            backtracking(ind+1);
            subset.pop();

            while(ind+1 < nums.length && nums[ind] === nums[ind+1]) {
                ind++;
            };
            backtracking(ind+1);
        }

        const res = [];
        const subset = [];
        nums.sort((a,b) => a-b);
        backtracking(0);
        return res;
    }
}
