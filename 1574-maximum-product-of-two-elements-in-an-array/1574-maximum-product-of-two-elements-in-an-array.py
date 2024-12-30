class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [(i-1)*-1 for i in nums]
        heapq.heapify(nums)
        first  = -heapq.heappop(nums)
        second = -heapq.heappop(nums)
        return first*second

        
        