class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        # 紀錄 fresh 的數量 => 變成 0 代表全部都腐爛
        # time: 該格在第幾個時間單位會被感染
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        # 四個可感染方向
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                
                # 四個方向個遍歷一次
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # 直接跳過 if:
                    # row, col outbound
                    # 該格已經是腐爛水果
                    if (row not in range(ROWS) or
                        col not in range(COLS) or
                        grid[row][col] != 1):
                        continue
                    
                    # 把那一格改成腐爛水果並加入 q 可以跑下一輪
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            
            # 每跑完一輪 q 就加一個時間單位跑下一輪
            time += 1

        return time if fresh == 0 else -1
                    
