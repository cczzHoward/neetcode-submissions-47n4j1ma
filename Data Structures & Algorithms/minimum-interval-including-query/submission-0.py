class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minHeap = [] # pair: (length, right point(end of interval))
        res, i = {}, 0

        # x.sort()  -> 對 x array 排序             (original array)
        # sorted(x) -> 複製出一個排序過後的 x array (new array)
        for q in sorted(queries):
            # 把這個 q 在範圍內的 interval 都加進 minHeap 裡面
            #     i 在範圍內(inbound) and 這個 q 是否包含在這個 interval 內(q >= interval's left point)
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1

            # 取最小值前把已經 outbound 的 interval 從 minHeap 中移除
            # * 如果有比合法最小值大的 "不合法interval" 不會被刪除 (因為不影響最小值所以無影響)
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            # 把最小值放進 res[q]
            res[q] = minHeap[0][0] if minHeap else -1
        
        # 用 list comprehension 來 mapping q -> res[q] 且 return
        return [res[q] for q in queries]