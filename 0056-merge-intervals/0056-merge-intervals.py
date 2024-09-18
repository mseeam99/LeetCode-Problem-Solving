class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda first : first[0])
        answer = [intervals[0]]
        for i in range(1,len(intervals)):
            lastValue = answer[-1][1]
            if intervals[i][0] <= lastValue:
                answer[-1][1] = max(lastValue,intervals[i][1])
            else:
                answer.append([intervals[i][0],intervals[i][1]])
        return answer
        