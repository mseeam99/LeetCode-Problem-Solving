class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True

        hashMapOne = {}
        hashMapTwo = {}

        changes = 0

        for i in range(len(s1)):

            if s1[i] != s2[i]:
                changes += 1
                if changes > 2:
                    return False
            
            if s1[i] not in hashMapOne:
                hashMapOne[s1[i]] = 1
            else:
                hashMapOne[s1[i]] += 1

            if s2[i] not in hashMapTwo:
                hashMapTwo[s2[i]] = 1
            else:
                hashMapTwo[s2[i]] += 1

        if hashMapOne == hashMapTwo:
            return True
        return False