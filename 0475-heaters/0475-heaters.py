class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()

        def linearIter(radius):
            intervals = []
            for h in heaters:
                left = h - radius
                right = h + radius
                intervals.append((left, right))
          #  intervals.sort()
            i = 0  
            j = 0 
            while j < len(houses) and i < len(intervals):
                left, right = intervals[i]
                if houses[j] < left:
                    return False  
                if left <= houses[j] <= right:
                    j += 1
                else:
                    i += 1
            return j == len(houses)

        left = 0
        right = max(max(houses), max(heaters)) - min(min(houses), min(heaters))
        answer = right
        while left <= right:
            middle = left + (right-left) // 2
            if linearIter(middle) == True:
                answer = min(answer,middle)
                right = middle - 1
            else:
                left = middle + 1
        return answer






        