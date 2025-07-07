class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = [i,0]
            else:
                hashMap[s[i]][1] = i
        for v in hashMap.values():
            if v[1] == 0:
                v[1] = v[0]

        answer = []
        leftPointer = 0
        partition = 0
        farthest = hashMap[s[0]][1] 
        
        while leftPointer < len(s):

            currentChar = s[leftPointer]
            currentFarthest = hashMap[currentChar][1]
            if currentFarthest > farthest:
                farthest = currentFarthest

            if leftPointer == farthest:
                partition = leftPointer - partition + 1
                answer.append(partition)
                partition = leftPointer + 1 
                
            leftPointer+=1
           
        return answer


