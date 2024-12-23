class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)
        while len(stones) > 1:
            one = heappop(stones) * -1
            two = heappop(stones) * -1
            if one != two:
                heapq.heappush(stones,-(one-two))
        return -stones[0] if stones else 0
