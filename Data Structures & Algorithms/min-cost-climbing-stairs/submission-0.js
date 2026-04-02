class Solution {
    /**
     * @param {number[]} cost
     * @return {number}
     */
    minCostClimbingStairs(cost) {
        let one = cost[cost.length-2];
        let two = cost[cost.length-1];
        let temp;

        for (let i = 0; i < cost.length-2; i++) {
            temp = cost[cost.length-3-i] + Math.min(one,two);
            two = one;
            one = temp;
        }

        return Math.min(one, two);
    }
}
