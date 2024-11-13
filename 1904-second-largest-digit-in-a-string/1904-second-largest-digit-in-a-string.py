class Solution:
    def secondHighest(self, s: str) -> int:
        mySet = set()
        for i in range(len(s)):
            if s[i].isnumeric():
                mySet.add(int(s[i]))
        myList = sorted(mySet, reverse=True)
        if len(myList) < 2:
            return -1
        return myList[1]