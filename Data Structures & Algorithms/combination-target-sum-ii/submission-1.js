class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    combinationSum2(candidates, target) {
        function backtracking(idx, comb, total) {
            if (total === target) {
                res.push([...comb]);
                return;
            }

            if (total > target || idx >= candidates.length) {
                return;
            }

            comb.push(candidates[idx]);
            backtracking(idx+1, comb, total+candidates[idx]);
            comb.pop();

            while (idx+1 < candidates.length && candidates[idx] === candidates[idx+1]) {
                idx++;
            }
            backtracking(idx+1, comb, total);
        };

        let res = [];
        candidates.sort((a,b)=>a-b);
        backtracking(0, [], 0);
        return res;
    }
}
