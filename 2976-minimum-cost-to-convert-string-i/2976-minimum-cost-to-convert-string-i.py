class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        hashMap = defaultdict(list)
        for i in range(len(original)):
            s, c, d = original[i], cost[i], changed[i]
            hashMap[s].append([c, d])  # cost, destination

        memo = {}

        def function(s, t):
            if (s, t) in memo:
                return memo[(s, t)]

            if s == t:
                memo[(s, t)] = 0
                return 0

            minHeap = [[0, s]]  # cost, destination
            heapq.heapify(minHeap)
            visitedSet = set()

            while minHeap:
                cost, destination = heapq.heappop(minHeap)

                if destination == t:
                    memo[(s, t)] = cost
                    return cost

                if destination in visitedSet:
                    continue
                visitedSet.add(destination)

                theOtherDestinationsList = hashMap[destination]
                for i in range(len(theOtherDestinationsList)):
                    newCost = theOtherDestinationsList[i][0] + cost
                    newDestination = theOtherDestinationsList[i][1]
                    heapq.heappush(minHeap, [newCost, newDestination])

            memo[(s, t)] = -1
            return -1

        totalCost = 0
        for i in range(len(source)):
            val = function(source[i], target[i])
            if val == -1:
                return -1
            totalCost += val

        return totalCost