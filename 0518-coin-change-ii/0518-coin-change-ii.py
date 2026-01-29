class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        answer = 0

        memo = [0] * (len(coins)+1)
        for i in range(len(coins)+1):
            memo[i] = [float("-inf")]*(amount+1)
                
        def recursion(index,currentAmount):
            nonlocal answer, memo

            if (index >= len(coins)) or (currentAmount > amount):
                return 0
            
            if currentAmount == amount:
                return 1
                
            if memo[index][currentAmount] != float("-inf"):
                return memo[index][currentAmount]

            pick = recursion(index,currentAmount + coins[index])
            notPick = recursion(index+1,currentAmount)

            memo[index][currentAmount] = pick + notPick
            return memo[index][currentAmount]
            
        return recursion(0,0)
