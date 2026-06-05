class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 4:
            return 0

        smallestArray = heapq.nsmallest(4,nums)
        smallestArray.sort()

        largestArray = heapq.nlargest(4,nums)
        largestArray.sort()

        minDifference = float("inf")
        for i in range(4):
            minDifference = min(minDifference,largestArray[i]-smallestArray[i])

        return minDifference