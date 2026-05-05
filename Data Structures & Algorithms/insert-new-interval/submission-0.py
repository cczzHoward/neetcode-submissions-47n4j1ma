class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # 如果插入的線的尾巴比 i 線的開頭小 -> 較小且沒連結 -> 把 newInterval 丟到 res 
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # 如果插入的線的開頭比 i 線的尾巴大 -> 較大且沒連結 -> 把 intervals[i] 丟到 res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # 上面兩個是沒相交的情況
            # else 則是有相交的情況 -> merge 
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res
        