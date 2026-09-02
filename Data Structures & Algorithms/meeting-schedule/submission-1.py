"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        data = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(data)):

            if data[i-1].end > data[i].start:
                return False
        
        return True
            

