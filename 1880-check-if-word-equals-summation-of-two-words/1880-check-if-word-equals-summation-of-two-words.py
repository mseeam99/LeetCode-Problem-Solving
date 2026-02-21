class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        hashMap = {}
        for i in range(1,27):
            hashMap[chr(96+i)] = i-1
        
        firstValue = ""
        secondValue = ""
        targetValue = ""
        
        for i in range(len(firstWord)):
            firstValue += str(hashMap[firstWord[i]])
        for i in range(len(secondWord)):
            secondValue += str(hashMap[secondWord[i]])
        for i in range(len(targetWord)):
            targetValue += str(hashMap[targetWord[i]])
        

        firstValue = int(firstValue)
        secondValue = int(secondValue)
        targetValue = int(targetValue)

        print(firstValue)
        print(secondValue)
        print(targetValue)

        if firstValue + secondValue == targetValue:
            return True
        else:
            return False

        
        