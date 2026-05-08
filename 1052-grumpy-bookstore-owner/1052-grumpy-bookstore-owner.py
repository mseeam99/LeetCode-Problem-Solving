class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
       
        currSatisfaction = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                currSatisfaction += customers[i]

        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        maxExtra = extra

        leftPointer = 0
        rightPointer = minutes

      
        while rightPointer <= len(customers)-1:
            if grumpy[rightPointer] == 1:
                extra += customers[rightPointer]

            if grumpy[leftPointer] == 1:
                extra -= customers[leftPointer]

            
            maxExtra = max(maxExtra,extra)
            
            rightPointer += 1
            leftPointer += 1
            

        return currSatisfaction + maxExtra



        

        


        