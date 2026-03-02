class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
    
        if len(s) != len(goal):
            return False
        
        if s == goal:
            hashMap = {}
            for i in range(len(s)):
                if s[i] not in hashMap:
                    hashMap[s[i]] = 1
                else:
                    hashMap[s[i]] += 1
            
            for key,val in hashMap.items():
                if val > 1:
                    return True
            return False
        else:

            firstIndex = -1
            secondIndex = -1

            for i in range(len(s)):
                
                if s[i] != goal[i]:

                    if firstIndex != -1 and secondIndex != -1:
                        return False

                    if firstIndex == -1:
                        firstIndex = i
                    else:
                        secondIndex = i
            
            if s[firstIndex] == goal[secondIndex] and s[secondIndex] == goal[firstIndex]:
                return True
            else:
                return False

            

                







        
        