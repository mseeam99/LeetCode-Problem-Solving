class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        stack = []
        heapq.heapify(nums)
        poppedCount = 0
        while nums:
            number = heapq.heappop(nums)
            if stack and number == stack[-1]:
                stack.pop()
                poppedCount += 1
            else:
                stack.append(number)
        return [poppedCount,len(stack)]
       