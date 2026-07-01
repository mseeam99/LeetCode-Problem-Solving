class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        tempLengthTrack = len(gas)
        totalGas  = sum(gas)
        totalCost = sum(cost)
        if totalGas < totalCost:
            return -1

        gas = gas + gas
        cost = cost + cost

        

        startingIndex = 0
        currentGas = 0

        for i in range(len(gas)):

            if i == (startingIndex + tempLengthTrack) and gas[i]-cost[i] > 0:
                return startingIndex
        
            currentGas += gas[i]-cost[i]

            if currentGas < 0:
                startingIndex = i+1
                currentGas = 0


        return startingIndex
                

            

        
        