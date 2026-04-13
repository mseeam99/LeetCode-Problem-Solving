class Solution:
    def addDigits(self, num: int) -> int:


        number = str(num)

        while len(number) != 1:

            tempNumber = 0

            for i in range(len(number)):

                tempNumber += int(number[i])
            
            number = str(tempNumber)

        return int(number)


        