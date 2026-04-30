class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        # linear time
        for x, y in points:
            # 我們不需要真的求他的距離, 我們只求最近的點
            # dist 已經符合這個需求了 不需要再多開根號 (除非他有要求回傳真的距離)
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        
        # 轉成 minHeap
        heapq.heapify(minHeap)
        # 拿 k 個出來 (取出 k 個最近的 point)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res