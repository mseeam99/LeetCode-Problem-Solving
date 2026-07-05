class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) <= 4:
            return 0

        smallest = heapq.nsmallest(4,nums)
        largest  = sorted(heapq.nlargest(4,nums))

        less = float("inf")

        for i in range(len(smallest)):
            less = min(less, abs(largest[i]-smallest[i]))

        return less