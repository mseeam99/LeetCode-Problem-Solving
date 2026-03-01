class Solution:
    def equalFrequency(self, word: str) -> bool:

        def checkfrequency(string):
            hashMap = {}
            for i in range(len(string)):
                if string[i] not in hashMap:
                    hashMap[string[i]] = 1
                else:
                    hashMap[string[i]] += 1
            minValue = min(hashMap.values())
            for key,val in hashMap.items():
                if val != minValue:
                    return False
            return True
                
        for i in range(len(word)):
            tempString = ""
            for j in range(0,i):
                tempString += word[j]
            for j in range(i+1,len(word)):
                tempString += word[j]
            ans = checkfrequency(tempString)
            if ans == True:
                return True

        return False
            


        
        



        
        
        
                
        
