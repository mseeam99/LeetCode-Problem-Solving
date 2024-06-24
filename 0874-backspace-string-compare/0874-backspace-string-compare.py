class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        listOfS = []
        for i in range(len(s)):
            if s[i] == "#":
                if len(listOfS) != 0:
                    listOfS.pop()
            else:
                listOfS.append(s[i])

        listOfT = []
        for i in range(len(t)):
            if t[i] == "#":
                if len(listOfT) != 0:
                    listOfT.pop()
            else:
                listOfT.append(t[i])

        return listOfS == listOfT

        






        
        