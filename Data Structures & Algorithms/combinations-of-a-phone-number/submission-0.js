class Solution {
    /**
     * @param {string} digits
     * @return {string[]}
     */
    letterCombinations(digits) {
        function bt(i) {
            if (i >= digits.length) {
                res.push(part.join(""));
                return;
            }

            for (let char of Obj[digits[i]]) {
                part.push(char);
                bt(i+1);
                part.pop();
            }
        }

        if (digits.length === 0) return [];
        const Obj = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        const res = [];
        const part = [];
        bt(0);
        return res;
    }
}
