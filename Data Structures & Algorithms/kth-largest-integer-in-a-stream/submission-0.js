class MinHeap {
    constructor() {
        this.data = [];
    }

    size() {return this.data.length};
    peek() {return this.data[0]};

    insert(val) {
        this.data.push(val);
        this._heapifyUp();
    }

    extractMin() {
        if (this.size() === 0) return null;
        if (this.size() === 1) return this.data.pop();
        const min = this.data[0];
        this.data[0] = this.data.pop();
        this._heapifyDown();
        return min;
    }
    
    _heapifyUp() {
        let index = this.size() - 1;
        while (index > 0) {
            const parentIndex = Math.floor((index-1)/2);
            if (this.data[index] < this.data[parentIndex]) {
                this._swap(index, parentIndex);
                index = parentIndex
            } else {
                break;
            }
        }
    }

    _heapifyDown(index = 0) {
        let leftChildIndex = index * 2 + 1;
        let rightChildIndex = index * 2 + 2;
        let smallest = index;

        if (leftChildIndex < this.size() && this.data[leftChildIndex] < this.data[smallest]) {
            smallest = leftChildIndex;
        }
        if (rightChildIndex < this.size() && this.data[rightChildIndex] < this.data[smallest]) {
            smallest = rightChildIndex;
        }
        if (smallest !== index) {
            this._swap(smallest, index);
            this._heapifyDown(smallest);
        }
    }

    _swap(i, j) {
        [this.data[i], this.data[j]] = [this.data[j], this.data[i]]
    }
}

class KthLargest {
    /**
     * @param {number} k
     * @param {number[]} nums
     */
    constructor(k, nums) {
        this.k = k;
        this.minHeap = new MinHeap();
        for (let num of nums) {
            this.add(num);
        }
    }

    /**
     * @param {number} val
     * @return {number}
     */
    add(val) {
        if (this.minHeap.size() < this.k) {
            this.minHeap.insert(val);
        } else if (val > this.minHeap.peek()) {
            this.minHeap.extractMin();
            this.minHeap.insert(val);
        }
        return this.minHeap.peek();
    }
}
