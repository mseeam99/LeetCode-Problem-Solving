class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        shortInterval = [meetings[0]]

        for i in range(1,len(meetings)):
            if meetings[i][0] <= shortInterval[-1][1]:
                shortInterval[-1][1] = max(shortInterval[-1][1],meetings[i][1])
            else:
                shortInterval.append(meetings[i])

        count = 0
        for i in range(len(shortInterval)):
            count += shortInterval[i][1] - shortInterval[i][0] + 1 

        return days - count

        
        
            