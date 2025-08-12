class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        answer = []
        if intervals:
            answer.append(intervals[0])
        count = 0
        for i in range(1,len(intervals)):
            if answer:
                if answer[-1][1] > intervals[i][0]:
                    answer[-1][1] = min(answer[-1][1],intervals[i][1])
                    count += 1
                    continue
            answer.append(intervals[i])  
        return count
                

