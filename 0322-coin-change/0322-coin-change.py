class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        outerdp = [float("inf")] * (amount + 1)
        outerdp[0] = 0 

        for i in range(amount + 1):
            if i % coins[0] == 0:
                outerdp[i] = i // coins[0]

        for row in range(1, len(coins)):
            innerdp = outerdp.copy()
            for col in range(amount + 1):
                notTake = outerdp[col]
                take = float("inf")
                if coins[row] <= col:
                    take = 1 + innerdp[col - coins[row]]
                innerdp[col] = min(take, notTake)
            outerdp = innerdp

        return -1 if outerdp[amount] == float("inf") else int(outerdp[amount])
