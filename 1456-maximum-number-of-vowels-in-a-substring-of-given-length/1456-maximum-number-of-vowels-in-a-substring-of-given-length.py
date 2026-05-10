class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowelCount = 0
        for i in range(k):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                vowelCount += 1

        maxVowelCount = vowelCount

        leftPointer = 0
        rightPointer = k

        while rightPointer <= len(s)-1:

            if s[rightPointer] == 'a' or s[rightPointer] == 'e' or s[rightPointer] == 'i' or s[rightPointer] == 'o' or s[rightPointer] == 'u':
                vowelCount += 1
                

            if s[leftPointer] == 'a' or s[leftPointer] == 'e' or s[leftPointer] == 'i' or s[leftPointer] == 'o' or s[leftPointer] == 'u':
                vowelCount -= 1



            
            maxVowelCount = max(maxVowelCount, vowelCount)

            rightPointer += 1
            leftPointer += 1

        

        return maxVowelCount
            

        



        