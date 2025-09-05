class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def linearSearch(array, bananaEatingRate, h):
            totalHourUsed = 0
            for i in range(len(array)):
                if array[i] <= bananaEatingRate:
                    totalHourUsed+=1
                else:
                    totalHourUsed += ceil(array[i]/bananaEatingRate)
            return totalHourUsed

        
        left = 1
        right = max(piles)
        while left <= right:
            middleValue = left + (right-left) // 2
            returnValue = linearSearch(piles,middleValue,h)
            if returnValue <= h:
                right = middleValue - 1
            else:
                left = middleValue + 1
        return left

       




            

        