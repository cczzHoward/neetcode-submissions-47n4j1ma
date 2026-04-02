class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    lengthOfLIS(nums) {
        let dp = new Array(nums.length).fill(1);

        // 從陣列尾巴到頭
        for (let i = nums.length-1; i >= 0; i--) {
            // 要從 i+1 比對到最後一個(n-1)
            for (let j = i+1; j < nums.length; j++) {
                if (nums[i] < nums[j]) {
                    // 取最大值
                    dp[i] = Math.max(dp[i], dp[j]+1)
                }
            }
        }

        return Math.max(...dp);
    }
}
