class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashMap = {}
        for i in range(len(sentence)):
            hashMap[sentence[i]] = i+1
        boolanswer = True
        for i in range(1,27):
            char = chr(64+i)
            lower = char.lower()
            if lower not in hashMap:
                boolanswer = False
                return boolanswer
        return boolanswer
        