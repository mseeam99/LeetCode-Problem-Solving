class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda i: (i[0], -i[1]))
        print(intervals)
        count = 0
        lastOne = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][1] <= lastOne[1]:
                count+=1
                continue
            lastOne = intervals[i]
        return len(intervals) - count

        
        