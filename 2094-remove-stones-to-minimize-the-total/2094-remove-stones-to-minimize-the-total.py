class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = []
        for i in range(len(piles)):
            maxHeap.append(piles[i] * -1)
        heapq.heapify(maxHeap)
        for i in range(k):
            current = heapq.heappop(maxHeap)
            newValue = floor(current/2)
            heapq.heappush(maxHeap,newValue)
        for i in range(len(maxHeap)):
            maxHeap[i] = maxHeap[i] * -1
        return sum(maxHeap)