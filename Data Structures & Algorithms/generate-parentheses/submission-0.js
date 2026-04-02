class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    backtracking(res, n, stack='', openN=0, closeN=0) {
        if (stack.length === n*2) {
            res.push(stack);
            return;
        }

        if (openN < n) {
            this.backtracking(res, n, stack+'(', openN+1, closeN);
        }

        if (closeN < openN) {
            this.backtracking(res, n, stack+')', openN, closeN+1);
        }
    }

    generateParenthesis(n) {
        let res = [];
        this.backtracking(res, n);
        return res;
    }
}
