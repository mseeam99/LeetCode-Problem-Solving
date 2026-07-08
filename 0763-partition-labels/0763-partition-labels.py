class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = i
            elif s[i] in hashMap:
                hashMap[s[i]] = i
        answer = []
        leftPointer = 0
        rightPointer = 0
        farthest = hashMap[s[0]]
        while rightPointer <= len(s)-1:
            farthest = max(farthest,hashMap[s[rightPointer]])
            if rightPointer == farthest:
                answer.append(rightPointer - leftPointer + 1)
                leftPointer = rightPointer + 1
            rightPointer += 1
        return answer