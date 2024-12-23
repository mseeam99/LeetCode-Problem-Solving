class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        theArray = heapq.nlargest(k,nums)
        return theArray[len(theArray)-1]
        