class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        count = 0
        for col in range(len(strs[0])):
            tempString = ""
            for row in range(len(strs)):
                tempString += strs[row][col]

            print(tempString)

                

           
            
            starting = ord(tempString[0])
            for i in range(len(tempString)):
                if ord(tempString[i]) < starting:
                    count += 1
                    break
                else:
                    starting = ord(tempString[i])
                
        
        return count




        

