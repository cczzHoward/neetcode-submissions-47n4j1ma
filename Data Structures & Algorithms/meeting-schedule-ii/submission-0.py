"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # start 存會議開始時間
        # end   存會議結束時間
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        start_ind, end_ind = 0, 0

        while start_ind < len(intervals):
            if start[start_ind] < end[end_ind]:
                # 有一個會議開始
                count += 1
                start_ind += 1
            # start[start_ind] >= end[end_ind]
            else:
                # edge case: 同一個時間有會議開始跟結束 
                # ^ 先跑 end 再跑 start 就不會多記, 所以 == 的狀況先跑下面這段再跑上面那段
                # 有一個會議結束
                count -= 1
                end_ind += 1
            
            # 更新最大的數字
            res = max(res, count)

        return res
            