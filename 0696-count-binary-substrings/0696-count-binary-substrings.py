class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        prev = 0
        curr = 1
        answer = 0

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                curr += 1
            
            elif s[i] != s[i-1]:
                answer += min(curr,prev)
                prev = curr
                curr = 1
            
            if i == len(s)-1:
                answer += min(curr,prev)

        return answer 


        