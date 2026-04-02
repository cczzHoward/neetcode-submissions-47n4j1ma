class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let stack = [];

        for (let token of tokens) {
            if (token === '+') {
                stack.push(stack.pop()+stack.pop());
            } else if (token === '-') {
                let e2 = stack.pop();
                let e1 = stack.pop();
                stack.push(e1-e2);
            } else if (token === '*') {
                stack.push(stack.pop() * stack.pop());
            } else if (token === '/') {
                let e2 = stack.pop();
                let e1 = stack.pop();
                stack.push(parseInt(e1/e2));
            } else {
                stack.push(parseInt(token));
            }
        }
        return stack[0];
    }
}
