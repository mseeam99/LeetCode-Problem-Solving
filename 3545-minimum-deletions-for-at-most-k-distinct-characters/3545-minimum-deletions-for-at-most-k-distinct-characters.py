class Solution:
    def minDeletion(self, s: str, k: int) -> int:

        frequencyArray = [0]*27

        for i in range(len(s)):
            current = ord(s[i])+1 - 97
            frequencyArray[current] += 1

        frequencyArray.sort()
        frequencyArray = frequencyArray[::-1]

        print(frequencyArray)

        count = 0

        for i in range(k,len(frequencyArray)):
            count += frequencyArray[i]




        return count 

        