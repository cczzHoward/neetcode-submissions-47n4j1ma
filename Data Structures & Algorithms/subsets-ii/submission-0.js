class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums) {
        function backtracking(ind) {
            res.push([...subset]);
            for (let i = ind; i < nums.length; i++) {
                if (i > ind && nums[i] === nums[i-1]) {
                    continue;
                }
                subset.push(nums[i]);
                backtracking(i+1);
                subset.pop();
            }    
        }

        const res = [];
        const subset = [];
        nums.sort((a,b) => a-b);
        backtracking(0);
        return res;
    }
}
