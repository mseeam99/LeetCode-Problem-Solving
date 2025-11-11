class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()

        def linearIter(radius):
            # Build intervals efficiently
            intervals = []
            for h in heaters:
                left = h - radius
                right = h + radius
                intervals.append((left, right))
            
            # Sort intervals by left bound
            intervals.sort()

            # Two-pointer sweep to check houses
            i = 0  # pointer for intervals
            j = 0  # pointer for houses

            while j < len(houses) and i < len(intervals):
                left, right = intervals[i]

                # If the house is smaller than interval start → move to next interval?
                if houses[j] < left:
                    return False  # this house can't be covered

                # If house fits inside interval → move to next house
                if left <= houses[j] <= right:
                    j += 1
                else:
                    # house > right → move to next interval
                    i += 1

            # After loop, if any houses remain → not covered
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






        