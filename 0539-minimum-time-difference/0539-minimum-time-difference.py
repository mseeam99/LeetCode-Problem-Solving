class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        timePoints.sort()
        newArray = []

        for i in range(len(timePoints)):
            array = timePoints[i].split(":")
            hour = int(array[0])
            minuites = int(array[1])
            newArray.append((hour * 60) + minuites)

        res = (60 * 24) - newArray[-1] + newArray[0]

        for i in range(len(newArray)-1):
            fast = newArray[i+1]
            slow = newArray[i]
            difference = int(fast)-int(slow)

            res = min(res,difference)

        return res




       

        

            
            
           