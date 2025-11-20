class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        for i in range(len(intervals)):
            intervals[i].append(i)

        sortedIntervals = intervals.copy()
        sortedIntervals.sort()

        def binarySearch(targetEnd):
            left = 0
            right = len(sortedIntervals) - 1
            res = len(sortedIntervals)  
            while left <= right:
                middle = left + (right - left) // 2
                middleStart = sortedIntervals[middle][0]
                if middleStart >= targetEnd:
                    res = middle      
                    right = middle - 1
                else:
                    left = middle + 1
            return res
            
        answer = []
        for i in range(len(intervals)):
            index = binarySearch(intervals[i][1])
            if index == len(sortedIntervals):
                answer.append(-1)     
            else:
                answer.append(sortedIntervals[index][2])        
        return answer




       

