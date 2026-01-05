class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        if len(num) == 1:
            return int(num)
        length = len(num)
        
        while length > 1:
            current = 0
            for i in range(len(num)):
                current += int(num[i])
            num = str(current)
            length = len(num)
            
        return int(num)




            





        