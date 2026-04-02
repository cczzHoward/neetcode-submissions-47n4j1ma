class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 將資料整理成 [[p1, s1], [p2, s2]...]
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        # 將 pair 按照離 target 遠近來排列後，反向遍歷
        for p, s in sorted(pair)[::-1]:
            # 算出這台車裡終點還要多少時間單位
            stack.append((target-p)/s)
            # 如果後車可以比前車更早抵達終點，那就刪除他(因為它會跟前車合併變成一個車隊)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # stack 內元素數量就是車隊數量
        return len(stack)