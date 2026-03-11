class Solution:
    def clearDigits(self, s: str) -> str:

        answer = []

        for i in range(len(s)):
            if "a" <= s[i] <= "z":
                answer.append(s[i])
            else:
                answer.pop()

        return "".join(answer)


        