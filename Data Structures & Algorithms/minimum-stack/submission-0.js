class MinStack {
    constructor() {
        this.stack = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        let current_min = this.getMin();
        if (current_min === null || val < current_min) current_min = val;
        this.stack.push([val, current_min]);
    }

    /**
     * @return {void}
     */
    pop() {
        return this.stack.pop();
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack.length ? this.stack[this.stack.length-1][0] : null;
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.stack.length ? this.stack[this.stack.length-1][1] : null;
    }
}
