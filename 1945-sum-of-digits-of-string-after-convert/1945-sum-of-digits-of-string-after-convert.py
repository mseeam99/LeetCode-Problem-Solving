class Solution:
    def getLucky(self, s: str, k: int) -> int:
        hashMap = {}
        for i in range(1,27):
            hashMap[chr(64+i).lower()] = i
        string = ""
        for i in range(len(s)):
            string += str(hashMap[s[i]])
        currentSum = 0
        for _ in range(1,k+1):
            currentSum = 0
            for i in range(len(string)):
                currentSum += int(string[i])
            string = str(currentSum)
        return int(currentSum)


