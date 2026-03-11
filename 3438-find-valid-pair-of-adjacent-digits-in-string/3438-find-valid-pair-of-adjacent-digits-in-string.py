class Solution:
    def findValidPair(self, s: str) -> str:
        answer = ""
        counter = Counter(s)
        for i in range(len(s)-1):
            if s[i] != s[i+1] and (counter[s[i]] == int(s[i])) and (counter[s[i+1]] == int(s[i+1])):
                answer += s[i]
                answer += s[i+1]
                break
        return answer



        
        