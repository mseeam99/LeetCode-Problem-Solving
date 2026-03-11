class Solution:
    def finalString(self, s: str) -> str:
        answer = []
        for i in range(len(s)):
            if s[i] == "i":
                answer = answer[::-1]
            else:
                answer.append(s[i])
        return "".join(answer)
        