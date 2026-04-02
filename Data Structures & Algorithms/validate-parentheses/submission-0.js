class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];
        for (let element of s) {
            if (element === '(' || element === '[' || element === '{') {
                stack.push(element);
            } else {
                if (!stack.length ||
                (element === ')' && stack[stack.length-1] !== '(') ||
                (element === ']' && stack[stack.length-1] !== '[') ||
                (element === '}' && stack[stack.length-1] !== '{') ) {
                    return false;
                }
                stack.pop();
            }
        }
        return !stack.length;
    }
}
