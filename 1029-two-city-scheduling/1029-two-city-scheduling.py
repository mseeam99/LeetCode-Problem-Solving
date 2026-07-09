class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs = sorted(costs, key=lambda x: (x[0] - x[1]))

        print(costs)

        length = len(costs)

        total = 0


        for i in range(0,length//2):
            total += costs[i][0]
            
        for i in range(length//2,len(costs)):
            total += costs[i][1]

        return total


        
        