class Solution:
    def minimumPushes(self, word: str) -> int:
        hashMap = Counter(word)
        word = list(word)
        for i in range(len(word)):
            word[i] = (-hashMap[word[i]],word[i])
        heapq.heapify(word)
        hashMap = {}
        hashMap["1"] = "EMPTY"
        clickedCount = 0
        while len(word):
            count,char = heapq.heappop(word)
            count = count*(-1)
            if char == "1" or char == "*" or char == "#" or char == "0":
                continue
            if char in hashMap:
                clickedCount += hashMap[char]  
            elif char not in hashMap:
                if len(hashMap) < 9:
                    hashMap[char] = 1
                    clickedCount += 1
                elif len(hashMap) < 17:
                    hashMap[char] = 2
                    clickedCount += 2
                elif len(hashMap) < 25:
                    hashMap[char] = 3
                    clickedCount += 3
                else:
                    clickedCount += 4
        return clickedCount

