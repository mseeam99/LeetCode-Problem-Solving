class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        fiveCount = 0
        tenCount = 0
        twentyCount = 0

        for i in range(len(bills)):

            if bills[i] == 5:
                fiveCount += 1

            elif bills[i] == 10:
                tenCount += 1
                if fiveCount == 0:
                    return False
                if fiveCount > 0:
                    fiveCount -= 1
                else:
                    return False
                
            elif bills[i] == 20:
                twentyCount += 1
                if fiveCount == 0:
                    return False
                if tenCount >= 1 and fiveCount >= 1:
                    tenCount -= 1 
                    fiveCount -= 1
                elif fiveCount >= 3:
                    fiveCount -= 3
                else:
                    return False

        return True





        