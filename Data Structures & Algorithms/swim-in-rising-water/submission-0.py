class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]] # pair: [grid, row, col]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))

        while minH:
            t, r, c = heapq.heappop(minH)
            # reach goal
            if r == N-1 and c == N-1:
                return t
            
            # 往四個方向嘗試
            for dr, dc in directions:
                neiR, neiC = r+dr, c+dc
                # 不成立的條件
                # outbound & visited
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit):
                    continue
                
                # 把可以走的路都加進 minHeap 裡面繼續遍歷
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
