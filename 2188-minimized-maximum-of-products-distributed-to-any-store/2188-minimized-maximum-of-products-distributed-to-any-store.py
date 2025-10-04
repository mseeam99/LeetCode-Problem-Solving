class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def checkIfPossible(maxproducts):
            nonlocal quantities, n
            j = 0
            currentProducts = quantities[j]
            for i in range(n):
                if currentProducts <= maxproducts:
                    currentProducts = 0 # after giving rest we have 0
                    j+=1
                    if j < len(quantities):
                        currentProducts = quantities[j]

                    if currentProducts == 0 and i <= n:
                        return True
                  
                else:
                    currentProducts -= maxproducts

            return False
                


        left = 0
        right = max(quantities)
        while left < right:
            middle = left + (right-left) // 2
            if checkIfPossible(middle) == True:
                right = middle
            else:
                left = middle + 1
        return left
            

        







        