class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canFinish(speed):
            totalHours = 0

            for bananas in piles:
                # hours needed for this pile
                if (bananas % speed ) != 0:
                    totalHours += (bananas // speed ) + 1
                else:
                    totalHours += (bananas // speed ) 

              

            return totalHours <= h

        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            if canFinish(mid):
                answer = mid      # valid → try smaller
                right = mid - 1
            else:
                left = mid + 1    # not valid → need faster

        return answer
        