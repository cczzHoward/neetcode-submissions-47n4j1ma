class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 每個元素照著 [0], [1] 的順序由小到大排
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # 如果沒有重疊 -> 不用刪除任何 interval -> 往下一個前進
            if start >= prevEnd:
                prevEnd = end
            # 如果重疊 -> 要記錄需要刪除的 interval(刪除 End 比較後面的)
            #                                     ^ 所以要留下 End 比較前面的
            else:
                # 紀要刪除的數量
                res += 1
                # 選擇留下 End 比較前面的
                prevEnd = min(prevEnd, end)
        
        return res