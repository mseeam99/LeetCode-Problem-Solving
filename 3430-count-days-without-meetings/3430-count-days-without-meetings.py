class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        shortInterval = [meetings[0]]

        print(meetings)

        for i in range(1,len(meetings)):
            if meetings[i][0] <= shortInterval[-1][1]:
                shortInterval[-1][1] = max(shortInterval[-1][1],meetings[i][1])
            else:
                shortInterval.append(meetings[i])

        print(shortInterval)

        # 1, 2, 3, 4 ,5, 6 , 7 , 8, 9, 10

        count = 0
        pointer = 1

        for i in range(len(shortInterval)):
            if i == 0:
                if shortInterval[i][0] != 1:
                    count += shortInterval[i][0] - 1
                    pointer = shortInterval[i][1] 
                else:
                    pointer = shortInterval[i][1] 

            if shortInterval[i][0] - pointer > 1:
                count += shortInterval[i][0] - pointer - 1
                pointer = shortInterval[i][1] 
            elif shortInterval[i][0] - pointer == 1:
                pointer = shortInterval[i][1] 

        if pointer < days:
            count += days - pointer
        

        return count
            



        
            
        
       



        return count




                


        