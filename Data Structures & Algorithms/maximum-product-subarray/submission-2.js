class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxProduct(nums) {
        let res = Math.min(...nums);
        let max = 1;
        let min = 1;
        
        for (let num of nums) {
            let temp = max;
            // 1. 找出本輪最大值
            max = Math.max(max * num, min * num, num);
            // 2. 找出本輪最小值
            min = Math.min(temp * num, min * num, num);
            // 3. 使用 res 記錄到目前為止的最大值
            res = Math.max(res, max);
        }

        return res;
    }
}
