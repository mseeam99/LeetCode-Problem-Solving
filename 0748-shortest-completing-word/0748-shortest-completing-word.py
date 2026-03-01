import copy
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        hashMap = {}
        for i in range(len(licensePlate)):
            if licensePlate[i].isdigit() == False and licensePlate[i] != " ":
                if licensePlate[i].lower() not in hashMap:
                    hashMap[licensePlate[i].lower()] = 1
                else:
                    hashMap[licensePlate[i].lower()] += 1
        
        answer = []

        for i in range(len(words)):
            copyHashMap = copy.deepcopy(hashMap)
            for j in range(len(words[i])):
                char = words[i][j]
                if char in copyHashMap:
                    copyHashMap[char]-=1
                else:
                    continue

            canReturn = True
            for key,val in copyHashMap.items():
                if val > 0:
                    canReturn = False
                    break
            if canReturn == True:
                answer.append(words[i])

        shortLength = float("inf")
        shortAns = ""
        for i in range(len(answer)):
            if len(answer[i]) < shortLength:
                shortAns = answer[i]
                shortLength = len(answer[i])

        return shortAns
            
                




        