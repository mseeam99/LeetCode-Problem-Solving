class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left = 0
        right = len(intervals)

        while left < right:
            middle = (left + right) // 2
            if intervals[middle][0] < newInterval[0]:
                left = middle + 1
                continue
            elif intervals[middle][0] > newInterval[0]:
                right = middle
                continue
            left+=1

        intervals.insert(left,newInterval)

        outerArray = []
        if intervals:
            outerArray.append(intervals[0])

        for i in range(1,len(intervals)):
            if outerArray:
                if outerArray[-1][1] >= intervals[i][0]:
                    outerArray[-1][1] = max(outerArray[-1][1],intervals[i][1])
                    continue
            outerArray.append(intervals[i])

        return outerArray