class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        function subrob(n) {
            let rob1 = 0;
            let rob2 = 0;
            let temp = 0;

            for (let robbing of n) {
                temp = Math.max(rob1 + robbing, rob2);
                rob1 = rob2;
                rob2 = temp;
            }

            return rob2;
        }
        return Math.max(nums[0], subrob(nums.slice(0,nums.length-1)), subrob(nums.slice(1)));
    }
}
