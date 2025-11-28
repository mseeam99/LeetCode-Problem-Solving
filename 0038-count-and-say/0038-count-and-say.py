class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        answer = "11"
        def takeAndReturn():
            nonlocal answer
            tempAnswer = ""
            pointerOne = 0
            pointerTwo = 0
            count = 0
            while pointerTwo < len(answer):
                if answer[pointerOne] == answer[pointerTwo]:
                    pointerTwo+=1
                    if pointerTwo == len(answer):
                        count = pointerTwo - pointerOne
                        tempAnswer+=str(count)
                        tempAnswer+=str(answer[pointerTwo-1])
                        break
                else:
                    count = pointerTwo - pointerOne 
                    pointerOne = pointerTwo
                    tempAnswer+=str(count)
                    tempAnswer+=str(answer[pointerTwo-1])
            answer = tempAnswer
        for i in range(3,n+1):
            takeAndReturn()
        return answer

        

        

        


        