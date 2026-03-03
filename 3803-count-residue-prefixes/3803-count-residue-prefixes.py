class Solution:
    def residuePrefixes(self, s: str) -> int:
        residueCount = 0
        mySet = set()

        for i in range(len(s)):
            mySet.add(s[i])
            if len(mySet) == (i + 1) % 3:
                residueCount+=1

        return residueCount