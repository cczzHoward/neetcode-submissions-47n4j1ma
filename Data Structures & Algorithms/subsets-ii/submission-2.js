class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums) {
        function bt(ind) {
            if (ind === nums.length) {
                res.push([...subset]);
                return;
            }

            subset.push(nums[ind]);
            bt(ind+1);
            subset.pop(nums[ind]);
            
            while (ind+1 < nums.length && nums[ind] === nums[ind+1]) {
                ind++;
            }
            bt(ind+1);
        }

        const res = [];
        const subset = [];
        nums.sort((a, b) => a-b);
        bt(0);
        return res;
    }
}
