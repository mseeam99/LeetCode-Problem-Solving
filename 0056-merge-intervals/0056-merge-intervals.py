class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        otherArray = []
        if intervals:
            otherArray.append(intervals[0])
        for i in range(1,len(intervals)):
            startValue = intervals[i][0]
            endValue = intervals[i][1]
            if otherArray:
                first = otherArray[-1][0]
                last = otherArray[-1][1]
                if startValue<=last:
                    otherArray[-1][1] = max(endValue,otherArray[-1][1])
                else:
                    otherArray.append(intervals[i])

        return otherArray
        