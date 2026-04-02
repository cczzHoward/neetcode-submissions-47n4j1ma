class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let left = 0
        let map = new Map();

        let res = 0
        for (let right = 0; right < s.length; right++) {
            while (map.has(s[right])) {
                map.delete(s[left]);
                left++;

            };
            map.set(s[right], 1);
            res = Math.max(res, right - left + 1);
        }
        return res;
    }
}
