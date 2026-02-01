class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        answer = float("+inf")
        memo = {}

        def recursion(index):
            nonlocal memo
            if index > len(cost):
                return 0
            
            if index == len(cost):
                return 0
            
            if index in memo:
                return memo[index]

            pickOne    = cost[index] + recursion(index+1)
            pickTwo    = cost[index] + recursion(index+2)
            returnMinimumAnswer = min(pickOne,pickTwo)
            memo[index] = returnMinimumAnswer
            return returnMinimumAnswer
    
        answer = min(answer,recursion(0))        
        answer = min(answer,recursion(1))         
        return answer