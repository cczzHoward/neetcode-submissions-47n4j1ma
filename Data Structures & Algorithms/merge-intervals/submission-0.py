class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 照著每一個 interval 的開頭排序
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        # intervals[0] 已經加進去了 -> 從 intervals[1] 開始遍歷
        for start, end in intervals[1:]:
            # 上一個 interval 的尾巴
            lastEnd = output[-1][1]

            # 跟前一個 interval 是否 overlapping
            # 有 overlapping -> merge
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            # 無 overlapping -> 直接放進 output
            else:
                output.append([start, end])
        
        return output

