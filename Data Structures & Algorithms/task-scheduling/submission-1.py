class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 建立 maxHeap
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]
        # 有東西還沒處理完的時候就要繼續跑
        while maxHeap or q:
            # 處理時間 +1
            time += 1
            if maxHeap:
                # 處理完後還待處理的數量
                cnt = 1 + heapq.heappop(maxHeap)
                # 如果還有數量 (>0), 就丟進 push 等 cooldown (n)
                if cnt:
                    q.append([cnt, time + n])
            
            # 如果 cooldown 時間到了, 可以丟回 maxHeap 等待處理
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        # 處理完後回傳處理時間
        return time