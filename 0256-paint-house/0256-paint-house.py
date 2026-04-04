class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        memo = {}

        def recursion(index,color):

            if (index,color) in memo:
                return memo[(index,color)]

            if index >= len(costs):
                return 0
            
            minimumCost = 0

            if color == 0:
                minimumCost = costs[index][color] + min(recursion(index+1,1),recursion(index+1,2))
            elif color == 1:
                minimumCost = costs[index][color] + min(recursion(index+1,0),recursion(index+1,2))
            if color == 2:
                minimumCost = costs[index][color] + min(recursion(index+1,0),recursion(index+1,1))
            
            memo[(index,color)] = minimumCost
            return minimumCost

        return min(recursion(0,0),recursion(0,1),recursion(0,2))
            

        