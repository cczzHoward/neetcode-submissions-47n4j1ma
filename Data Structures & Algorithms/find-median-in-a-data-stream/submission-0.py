class MedianFinder:
    def __init__(self):
        # self.small 裡面所有的數字都小於 self.large
        # self.small 是 maxHeap -> 取最大的數字 (mediam)
        # self.large 是 minHeap -> 取最小的數字 (mediam)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # 預設丟進 self.small 後再來判斷及處理
        heapq.heappush(self.small, -num)

        # 確認 self.small 裡的數字都小於 self.large
        # 如果 max(self.small) > min(self.large)
        # -> 把 max(self.small) 丟去 self.large
        if (self.small and self.large and
            -self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # self.small & self.large 的數量差距要在 1 以內
        # self.small 太多數字
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # self.large 太多數字
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # self.small 數字比 self.large 多
        if len(self.small) > len(self.large):
            return -self.small[0]
        # self.large 數字比 self.small 多
        if len(self.large) > len(self.small):
            return self.large[0]
        # self.small 與 self.large 數字數量相同 (總數有偶數個)
        return (-self.small[0] + self.large[0]) / 2
        
        