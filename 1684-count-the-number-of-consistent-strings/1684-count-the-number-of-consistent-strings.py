class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashMap = {}
        for i in range(len(allowed)):
            if allowed[i] not in hashMap:
                hashMap[allowed[i]] = 1
            else:
                hashMap[allowed[i]] += 1
        count = 0
        for i in range(len(words)):
            isItCountable = True
            for j in range(len(words[i])):
                if words[i][j] not in hashMap:
                    isItCountable = False
            if isItCountable == True:
                count += 1
        return count
                