class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        pointerOne = len(num1)-1
        pointerTwo = len(num2)-1

        carry = 0
        answer = ""
        
        while pointerOne >= 0 or pointerTwo >= 0 or carry:

            n1, n2 = 0,0

            if pointerOne >= 0:
                n1 = int(num1[pointerOne])
            else:
                n1 = 0
            
            if pointerTwo >= 0:
                n2 = int(num2[pointerTwo])
            else:
                n2 = 0
                
            currentSum = n1 + n2
            currentSum += carry
            carry = 0

            if int(currentSum) <= 9:
                answer += str(int(currentSum))
            elif int(currentSum) >= 10:
                answer += str(int(currentSum) % 10)
                carry = floor(int(currentSum)/10)
            
            pointerOne-=1
            pointerTwo-=1
        
        if carry != 0:
            answer += str(carry)

        return answer[::-1]

        







        