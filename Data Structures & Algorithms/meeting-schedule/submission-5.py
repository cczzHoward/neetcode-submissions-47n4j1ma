"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Solution 2
        if not intervals:
            return True

        intervals.sort(key = lambda i : i.start)
        prevEnd = intervals[0].end
        for interval in intervals[1:]:

            # overlapping -> False
            if interval.start < prevEnd:
                return False
            
            # 更新 prevEnd
            prevEnd = interval.end
            
        return True