class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}

        def recursion(index,currentCost):

            nonlocal memo

            if index >= len(cost):
                return 0
          
            if index in memo:
                return memo[index]

            oneStep = cost[index] + recursion(index+1,currentCost+cost[index])
            twoStep = cost[index] + recursion(index+2,currentCost+cost[index])

            memo[index] = min(oneStep,twoStep)
            return memo[index]


        answer1 = recursion(0,0)
        answer2 = recursion(1,0)
        return min(answer1,answer2)

        

            
            



        