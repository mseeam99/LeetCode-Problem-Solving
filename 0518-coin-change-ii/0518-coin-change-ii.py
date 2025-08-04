class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        outerdp = [0] * (amount + 1)
        
        for T in range(amount + 1):
            outerdp[T] = int(T % coins[0] == 0)

        for row in range(1, len(coins)):
            innerdp = outerdp.copy()
            for col in range(amount + 1):
                notTake = outerdp[col]
                take = 0
                if coins[row] <= col:
                    take = innerdp[col - coins[row]]
                innerdp[col] = take + notTake
            outerdp = innerdp

        return outerdp[amount]
