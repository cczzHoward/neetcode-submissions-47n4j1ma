class Solution {
    /**
     * @param {string} s
     * @return {string[][]}
     */
    partition(s) {
        function bt (i) {
            if (i >= s.length) {
                res.push([...part]);
                return;
            }

            for (let j = i; j < s.length; j++) {
                if (isPali(i, j)) {
                    part.push(s.substring(i, j+1));
                    bt(j+1);
                    part.pop();
                }
            }
        };

        function isPali(l, r) {
            while (l < r) {
                if (s[l] !== s[r]) {
                    return false;
                }
                l++;
                r--;
            }
            return true;
        };

        const res = [];
        const part = [];
        bt(0);
        return res;

    }
}
