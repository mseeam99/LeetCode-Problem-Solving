class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 1:
            return True
        intervals.sort()
        for i in range(1,len(intervals)):
            currentInterval = intervals[i]
            previousInterval = intervals[i-1]
            if currentInterval[0] < previousInterval[1]:
                return False
        return True



        