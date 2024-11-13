class Solution:
    def toLowerCase(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            answer += s[i].lower()
        return answer
        