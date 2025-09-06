import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def linear(weights,perDayCapacity):
            dayCount = 0
            weightCount = 0
            for i in range(len(weights)):
                weightCount += weights[i]
                if weightCount > perDayCapacity:
                    dayCount += 1
                    weightCount = weights[i]       
            return dayCount

        totalWeight = sum(weights)
        left = max(weights)
        right = totalWeight
        while left <= right:
            middle = left + (right - left) // 2
            daysNeeded = linear(weights,middle)
            if daysNeeded >= days:           # means rate is smaller
                left = middle + 1
            else:                            # means rate is bigger
                right = middle - 1
        return left





        