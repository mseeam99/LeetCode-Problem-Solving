class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashMap = {}
        for i in range(len(keyboard)):
            hashMap[keyboard[i]] = i

        time = 0
        for i in range(len(word)):
            if i == 0:
                time += hashMap[word[i]]
            else:
                time += abs(hashMap[word[i]] - hashMap[word[i-1]])



        return time

        

        


        