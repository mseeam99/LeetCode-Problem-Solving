class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = []
        end   = []

        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])

        start.sort()
        end.sort()
        
        pointerOne = 0
        pointerTwo = 0

        result = 0 
        count  = 0

        while pointerOne < (len(intervals)):
            if start[pointerOne] < end[pointerTwo]:
                count+=1
                pointerOne+=1
            else:
                count-=1
                pointerTwo+=1
            result = max(count,result)

        return result



        