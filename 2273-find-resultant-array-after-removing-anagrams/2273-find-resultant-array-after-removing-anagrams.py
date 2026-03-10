class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def compare(string1,string2):
            if len(string1) != len(string2):
                return False
            hashMap = {}
            for i in range(len(string1)):
                if string1[i] not in hashMap:
                    hashMap[string1[i]] = 1
                else:
                    hashMap[string1[i]] += 1
            for i in range(len(string2)):
                if string2[i] in hashMap:
                    hashMap[string2[i]] -= 1
            for key,val in hashMap.items():
                if val != 0:
                    return False
            return True
                
        answer = [words[0]]
        for i in range(1,len(words)):
            if compare(words[i],answer[-1]) == True:
                continue
            answer.append(words[i])
        
        return answer








        