class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for i in range(len(banned)):
            banned[i] = banned[i].lower()
        hashMap = {}
        eachWord = ""

        for i in range(len(paragraph)):
            char = paragraph[i]
            if char.isalpha():
                eachWord+=char
            else:
                if eachWord:
                    if eachWord not in hashMap:
                        hashMap[eachWord] = 1
                    else:
                        hashMap[eachWord] += 1
                eachWord = ""

        if eachWord not in hashMap:
            hashMap[eachWord] = 1
        else:
            hashMap[eachWord]+=1

        for i in range(len(banned)):
            if banned[i] in hashMap:
                hashMap[banned[i]] = ""

        maxString = ""
        tempVal = 0

        print(hashMap)

        for key,val in hashMap.items():
            if val == "":
                continue
            if val > tempVal:
                tempVal = val
                maxString = key

        return maxString



      


        