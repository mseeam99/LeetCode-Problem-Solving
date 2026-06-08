class Solution:
    def minSwaps(self, data: List[int]) -> int:

        oneCount = data.count(1)

        leftPointer = 0
        rightPointer = oneCount

        globalMinSwapNeeded = float("inf")

        curretSwapNeeded = 0

        for i in range(leftPointer,rightPointer):
            if data[i] == 0:
                curretSwapNeeded += 1
        
        globalMinSwapNeeded = min(globalMinSwapNeeded,curretSwapNeeded)

        leftPointer += 1

        while rightPointer < len(data):

            
            if data[rightPointer] == 0:
                curretSwapNeeded += 1
            
            
            if data[leftPointer-1] == 0:
                curretSwapNeeded -= 1
            
            
            globalMinSwapNeeded = min(globalMinSwapNeeded,curretSwapNeeded)

            leftPointer += 1
            rightPointer += 1


        return globalMinSwapNeeded


        





       


        