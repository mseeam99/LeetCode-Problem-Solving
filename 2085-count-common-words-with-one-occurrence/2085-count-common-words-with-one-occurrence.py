class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        minLength = ""
        maxLength = ""
        if len(words1) < len(words2):
            minLength = words1
            maxLength = words2
        else:
            minLength = words2
            maxLength = words1


        hashMap = {}
        for i in range(len(maxLength)):
            if maxLength[i] not in hashMap:
                hashMap[maxLength[i]] = 1
            else:
                hashMap[maxLength[i]] += 1

        for i in range(len(minLength)):
            if minLength[i] in hashMap:
                if hashMap[minLength[i]] > 1:
                    continue
                else:
                    hashMap[minLength[i]] -= 1

        print(hashMap)
        count = 0
        for key,val in hashMap.items():
            if val == 0:
                count += 1
        return count 
        



        