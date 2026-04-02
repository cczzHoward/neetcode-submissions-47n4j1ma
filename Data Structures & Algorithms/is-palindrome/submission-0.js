class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0;
        let r = s.length-1;

        while (l<r) {
            while (l<r && !/[a-zA-Z0-9]/.test(s[l])) l++;
            while (l<r && !/[a-zA-Z0-9]/.test(s[r])) r--;

            if (s[r].toLowerCase() !== s[l].toLowerCase()) return false;

            l++;
            r--;
        }
        return true;
    }
}
