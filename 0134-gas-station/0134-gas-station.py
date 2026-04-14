class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas  = sum(gas)
        totalCost = sum(cost)
        if totalGas < totalCost:
            return -1
        startingIndex = 0
        currentCost = 0
        for i in range(len(gas)):
            currentCost += gas[i]-cost[i]
            if currentCost < 0:
                startingIndex = i + 1
                currentCost = 0
        return startingIndex
        
        