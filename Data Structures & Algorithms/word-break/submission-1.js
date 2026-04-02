class Solution {
    /**
     * @param {string} s
     * @param {string[]} wordDict
     * @return {boolean}
     */
    wordBreak(s, wordDict) {
        let dp = new Array(s.length + 1).fill(false);
        dp[s.length] = true;

        for (let i = s.length; i >= 0; i--) {
            for (let word of wordDict) {
                // 對比單字不會超出陣列 and 單字是否相等
                if (i+word.length <= s.length && s.slice(i,i+word.length) === word) {
                    dp[i] = dp[i+word.length];
                }

                if (dp[i]) break;
            }
        }

        return dp[0];
    }
}
