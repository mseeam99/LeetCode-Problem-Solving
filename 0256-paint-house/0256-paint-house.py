class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        minCost = float("inf")
        memo = {}

        def recursion(index,color):
            nonlocal memo

            if (index, color) in memo:
                return memo[(index, color)]

            if index >= len(costs):
                return 0

            totalCost = 0

            
            if color == 0:
                totalCost = costs[index][color] + min(recursion(index+1,1) , recursion(index+1,2))
            elif color == 1:
                totalCost = costs[index][color] + min(recursion(index+1,0) , recursion(index+1,2))
            else:
                totalCost = costs[index][color] + min(recursion(index+1,0) , recursion(index+1,1))
            
            memo[(index, color)] = totalCost
            return memo[(index, color)]
           

            



        
        return min(recursion(0,0),recursion(0,1),recursion(0,2))
            

        
        