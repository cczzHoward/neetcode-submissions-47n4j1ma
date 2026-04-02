class MaxHeap {
    constructor() {
        this.data = [];
    }

    size() {return this.data.length}
    
    insert(val) {
        this.data.push(val);
        this._heapifyUp();
    }
    
    extractMax() {
        this._swap(0, this.size()-1);
        let max = this.data.pop();
        this._heapifyDown();
        return max;
    }

    _heapifyDown(index = 0) {
        let leftChildIndex = index*2 + 1;
        let rightChildIndex = index*2 + 2;
        let biggest = index

        if (leftChildIndex < this.size() && this.data[leftChildIndex] > this.data[biggest]) {
            biggest = leftChildIndex;
        }
        if (rightChildIndex < this.size() && this.data[rightChildIndex] > this.data[biggest]) {
            biggest = rightChildIndex;
        }
        if (biggest !== index) {
            this._swap(index, biggest);
            this._heapifyDown(biggest);
        }
    }

    _heapifyUp() {
        let index = this.size() - 1;
        while (index > 0) {
            let parentIndex = Math.floor((index-1)/2);
            if (this.data[parentIndex] < this.data[index]) {
                this._swap(parentIndex, index);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    _swap(i, j) {
        [this.data[i], this.data[j]] = [this.data[j], this.data[i]];
    }
}
class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        let maxHeap = new MaxHeap();
        for (let stone of stones) {
            maxHeap.insert(stone);
        }
        console.log(maxHeap.data);
        while (maxHeap.size() > 1) {
            let stone1 = maxHeap.extractMax();
            let stone2 = maxHeap.extractMax();
            if (stone1 !== stone2) {
                maxHeap.insert(Math.abs(stone1 - stone2))
            }
        }
        
        return maxHeap.size() > 0 ? maxHeap.data[0] : 0;
    }
}
