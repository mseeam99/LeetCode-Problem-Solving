class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        number = list(number)
        maxNumber = 0
        for i in range(len(number)):
            if number[i] == digit:
                newNumber = number[:i] + number[i+1:]
                currentNumber = int("".join(newNumber))
                maxNumber = max(maxNumber,currentNumber)
        return str(maxNumber)
            



                

        