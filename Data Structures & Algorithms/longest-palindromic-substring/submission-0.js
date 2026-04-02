class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    longestPalindrome(s) {
        let l = 0;
        let r = 0;
        let longestL = 0;
        let res = "";

        for (let i = 0; i < s.length; i++) {
            l = i;
            r = i;
            while (l >= 0 && r < s.length && s[l] === s[r]) {
                if ((r-l+1) > longestL) {
                    res = s.slice(l, r+1);
                    longestL = r-l+1;
                }
                l--;
                r++;
            }

            l = i;
            r = i+1;
            while (l >= 0 && r < s.length && s[l] === s[r]) {
                if ((r-l+1) > longestL) {
                    res = s.slice(l, r+1);
                    longestL = r-l+1;
                }
                l--;
                r++;
            }
        }
        return res;
    }
}
