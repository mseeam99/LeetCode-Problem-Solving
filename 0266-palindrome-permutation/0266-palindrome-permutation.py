class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        mySet = set()

        for i in range(len(s)):
            if s[i] in mySet:
                mySet.remove(s[i])
            else:
                mySet.add(s[i])
        
        if len(mySet) > 1:
            return False
        else:
            return True


        