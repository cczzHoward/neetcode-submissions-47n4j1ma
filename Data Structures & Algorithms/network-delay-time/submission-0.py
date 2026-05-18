class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's algorithm
        # 今天好想睡覺 狀態不好
        # 這題也比較複雜 一定要複習

        # Time Complexity (Edge * log Node)

        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            # 把這個 node 所有可走的下一步都加進 minHeap
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visit) == n else -1
                