'''
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        tableAsList = []

        tableAsList.append("0")
        tempValue = ""

        index = 1
        while index < n:
            tempListValue = tableAsList[index-1]
            newValue = ""
            innderIndex = 0
            while innderIndex < len(tempListValue):
                if tempListValue[innderIndex] == "0":
                    newValue+="01"
                elif tempListValue[innderIndex] == "1":
                    newValue+="10"
                innderIndex+=1
            tableAsList.append(newValue)
            index+=1
        
        strAnswer = tableAsList[n-1][k-1]
        answer = int(strAnswer)
        return answer
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
            
        length = 2 ** (n - 1)
        
        mid = length // 2
        
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - mid)




