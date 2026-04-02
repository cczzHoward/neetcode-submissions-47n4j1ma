class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    numDecodings(s) {
        function bt(i) {
            if (i === s.length) {
                res++;
                return;
            };
            if (s[i] === '0') return 0;

            bt(i+1);
            if (i < s.length - 1) {
                if (s[i] === '1' ||
                    s[i] === '2' && s[i+1] < '7') {
                    bt(i+2);
                }
            }
            return res;
        }
        let res = 0;
        bt(0);
        return res;
    }
}
