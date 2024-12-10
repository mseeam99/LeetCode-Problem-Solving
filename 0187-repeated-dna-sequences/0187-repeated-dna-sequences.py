class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        hashMap = {}
        tempString = ""
        index = 0
        for i in range(len(s)-9):
            index = i
            target = index + 10
            while index < target:
                tempString += s[index]
                index += 1
            if tempString not in hashMap:
                hashMap[tempString] = 1
                tempString = ""
            else:
                hashMap[tempString]+=1
                tempString = ""

        answer = []
        k = list(hashMap.keys())
        v = list(hashMap.values())

        for i in range(len(v)):
            if v[i] > 1:
                answer.append(k[i])
                
        return answer