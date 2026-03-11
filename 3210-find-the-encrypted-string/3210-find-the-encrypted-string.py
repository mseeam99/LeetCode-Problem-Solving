class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        s = list(s)
        answer = []
        for i in range(len(s)):
            char = s[(i+k)%len(s)]
            answer.append(char)
        return "".join(answer)


        