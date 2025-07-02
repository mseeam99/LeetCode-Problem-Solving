class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        index = 0
        totalSum = 0

        for i in range(len(cost)):
            totalSum += gas[i] - cost[i]

            if totalSum < 0:
                totalSum = 0
                index = i+1

        return index

      