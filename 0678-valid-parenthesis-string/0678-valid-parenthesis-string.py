class Solution:
    def checkValidString(self, s: str) -> bool:

        countMin = 0
        countMax = 0

        for i in range(len(s)):

            if s[i] == "(":
                countMin += 1
                countMax += 1

            elif s[i] == ")":
                countMin -= 1
                countMax -= 1

            else:
                countMin -= 1
                countMax += 1

            if countMin < 0:
                countMin = 0
            if countMax < 0:
                return False

        return countMin == 0

        




        