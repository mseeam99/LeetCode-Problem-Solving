class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        total   = sum(stones)
        target  = (total // 2)
        memo    = {}

        def recursion(index,currentSum):

            if currentSum >= target or index >= len(stones):
                return (abs(currentSum-(total-currentSum)))

            if (index,currentSum) in memo:
                return memo[(index,currentSum)]

            #pick
            pick = recursion(index+1, currentSum + stones[index])
            #not pick
            notPick = recursion(index+1, currentSum + 0 )

            answer = min(pick,notPick)

            memo[(index,currentSum)] = answer

            return answer

        return recursion(0,0)        