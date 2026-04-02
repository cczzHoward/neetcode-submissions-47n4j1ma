class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let obj = {};
        let ans = [];
        for (let num of nums) {
            if (!obj[num]) {
                obj[num] = 1;
            } else {
                obj[num]++;
            }
        }
        obj = Object.entries(obj).sort((a,b) => b[1]-a[1]);
        for (let num of obj) {
            if (k==0) break;
            ans.push(Number(num[0]));
            k--;
        }
        return ans;
    }
}
