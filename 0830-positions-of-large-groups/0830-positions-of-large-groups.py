class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        answer = []
        lastChar = s[0]
        pointer = 0
        count = 0
        while pointer <= len(s)-1:
            while pointer <= len(s)-1 and s[pointer] == lastChar:
                count+=1
                pointer+=1
            if count >= 3:
                answer.append([pointer-count,pointer-1])
            if pointer <= len(s)-1:
                lastChar = s[pointer]
            count = 0
        return answer