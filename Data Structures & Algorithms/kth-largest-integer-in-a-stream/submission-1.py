class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k

        # 把 self.minHeap 的 data structure 從 array 變成 minHeap
        heapq.heapify(self.minHeap)

        # 如果 minHeap 比 k 大 => 刪到跟 k 相等
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        # 把新數字推進 minHeap
        heapq.heappush(self.minHeap, val)

        # 因為 init 的時候 heap 長度有機會比 k 小
        # 所以有這行判定
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # idx 0 就是 heap 裡最小的數字
        # O(1)
        return self.minHeap[0]        
