class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let ans = {};

        for (let e of strs) {
            let key = e.split("").sort().join('');
            if (!ans[key]) {
                ans[key] = [];
            }
            ans[key].push(e);
        }
        
        return Object.values(ans)
    }
}
