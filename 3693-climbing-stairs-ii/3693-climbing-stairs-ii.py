class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        memo = {}

        def recursion(index, prevIndex):

            if index > n:
                return float("inf")
                
            if index == n:
                return 0

            if (index, prevIndex) in memo:
                return memo[(index, prevIndex)]

            answer = float("inf")

            if index + 1 <= n:
                j = index + 1
                jumpOneScore = costs[j - 1] + (1 * 1) #difference 1
                answer = min(answer, jumpOneScore + recursion(j, index))

            if index + 2 <= n:
                j = index + 2
                jumpTwoScore = costs[j - 1] + (2 * 2)  #difference 2
                answer = min(answer, jumpTwoScore + recursion(j, index))

            if index + 3 <= n:
                j = index + 3
                jumpThreeScore = costs[j - 1] + (3 * 3) #difference 3
                answer = min(answer, jumpThreeScore + recursion(j, index))

            memo[(index, prevIndex)] = answer
            return answer

        return recursion(0, -1)
