class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n + 1)
        for i in range(n+1):
            binaryrepresentation = str(bin(i))
            OneCount = 0
            for j in range(len(binaryrepresentation)):
                if binaryrepresentation[j] == "1":
                    OneCount+=1
            answer[i] = OneCount
        return answer
        
        