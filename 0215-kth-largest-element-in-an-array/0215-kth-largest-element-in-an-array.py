class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        answer = heapq.nlargest(k,nums)
        return answer[-1]
        