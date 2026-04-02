class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a,b)=>a-b);
        let res = [];

        for (let i = 0; i < nums.length-1; i++) {
            // 如果現在算的(nums[i])跟前一個(nums[i-1])算的是一樣的數字就可以跳過，不然會重複計算。
            if (i > 0 && nums[i] === nums[i-1]) continue;

            let j = i + 1;
            let k = nums.length - 1;

            
            while (j < k) {
                let total = nums[i] + nums[j] + nums[k];
                if (total < 0) {
                    j++;
                } else if (total > 0) {
                    k--;
                } else {
                    res.push([nums[i], nums[j], nums[k]]);
                    j++;
                    while(nums[j] === nums[j-1] && j < k) {
                        j++;
                    }
                }
            }
        }
        return res;
        
    }
}
