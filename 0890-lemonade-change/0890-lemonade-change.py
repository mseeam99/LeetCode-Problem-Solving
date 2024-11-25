class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        fiveNote = 0
        TenNote  = 0
        twenty   = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                fiveNote += 1
            else:
                recievedNote = bills[i]
                if recievedNote == 10:
                    TenNote += 1
                    mustBackMoney = 5
                    if fiveNote >= 1:
                        fiveNote -= 1
                    else:
                        return False
                if recievedNote == 20:
                    twenty += 1
                    mustBackMoney = 15
                    if fiveNote >= 1 and TenNote >= 1:
                        fiveNote -= 1
                        TenNote -= 1
                    elif fiveNote >= 3 :
                        fiveNote -= 3
                    else:
                        return False
                        
        return True