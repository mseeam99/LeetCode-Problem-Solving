class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        answer = []
        lo = 0
        hi = len(s)

        for i in range(len(s)):
            if s[i] == "I":
                answer.append(lo)
                lo+=1
            else:
                answer.append(hi)
                hi-=1

        answer.append(hi)
        return answer