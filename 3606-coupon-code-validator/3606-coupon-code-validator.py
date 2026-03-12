class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        def checkIsCodeValid(code):
            if code == "":
                return False
            returnStatement = True
            for i in range(len(code)):
                if (code[i].isalnum() == True):
                    continue
                elif (code[i].isalnum() == False) and (code[i] != "_"):
                    returnStatement = False
                    break
            return returnStatement

        array = []
        hashMap = {}
        hashMap["electronics"] = 1
        hashMap["grocery"] = 2
        hashMap["pharmacy"] = 3
        hashMap["restaurant"] = 4
        
        for i in range(len(code)):
            if (checkIsCodeValid(code[i]) == True) and (businessLine[i] == "electronics" or businessLine[i] == "grocery" or businessLine[i] == "pharmacy" or businessLine[i] == "restaurant") and isActive[i] == True:
                array.append((hashMap[businessLine[i]],code[i]))

        newArray = []
        heapq.heapify(array)
        while array:
            number, val = heapq.heappop(array)
            newArray.append(val)
        return newArray