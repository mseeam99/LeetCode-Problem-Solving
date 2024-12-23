class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        theArray = heapq.nlargest(k,nums)

        print(theArray)
        return theArray[len(theArray)-1]
        