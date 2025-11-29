class Solution:
    def removeVowels(self, s: str) -> str:
        mySet = set()
        mySet.add("a")
        mySet.add("e")
        mySet.add("i")
        mySet.add("o")
        mySet.add("u")
        mySet.add("A")
        mySet.add("E")
        mySet.add("I")
        mySet.add("O")
        mySet.add("U")
        answer = ""
        for i in range(len(s)):
            if s[i] in mySet:
                continue
            else:
                answer+=s[i]
        return answer

        