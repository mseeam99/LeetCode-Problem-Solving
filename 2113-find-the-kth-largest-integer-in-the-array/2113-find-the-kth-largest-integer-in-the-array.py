class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        for i in range(len(nums)):
            s = nums[i]
            nums[i] = int(s)
        heapq.heapify(nums)
        newArray = heapq.nlargest(k,nums)
        newArray = newArray[::-1]
        return str(newArray[0])

        
        