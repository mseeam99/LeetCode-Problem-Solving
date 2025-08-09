class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        cleanString = ""
        for i in range(len(s)):
            if s[i] == "-":
                continue
            else:
                cleanString+=s[i].upper()

        answer = ""
        indexTrack = 0
        for i in range(len(cleanString)-1,-1,-1):
            if indexTrack == k:
                answer+="-"
                indexTrack = 0
            answer+=cleanString[i]
            indexTrack+=1
            
        return answer[::-1]
        