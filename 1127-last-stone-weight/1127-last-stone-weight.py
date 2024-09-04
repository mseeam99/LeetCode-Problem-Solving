class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        while len(stones) > 1:
            firstTwoElements = heapq.nlargest(2,stones)
            stones.remove(firstTwoElements[0])
            stones.remove(firstTwoElements[1])
            if firstTwoElements[0] != firstTwoElements[1]:
                tempValue = firstTwoElements[0] - firstTwoElements[1]
                heapq.heappush(stones,tempValue)
        return stones[0] if stones else 0

        
        