class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num2Index = len(num2)-1
        answer = ""
        store = []
        
        track = 0
        while num2Index >= 0:
            carry = 0
            for i in range(len(num1)-1,-1,-1):
                totalValue = (int(num2[num2Index]) * int(num1[i])) + carry
                carry = totalValue // 10
                currentAddingValue = (totalValue - (carry*10))
                answer += str(currentAddingValue)

            if carry != 0:
                answer += str(carry)

            answer = answer[::-1]
            for i in range(track):
                answer += "0"           
            track += 1

            store.append(answer)
            answer = ""
            num2Index -= 1
        
        answer = 0
        for i in range(len(store)):
            answer += int(store[i])
        answer = str(answer)
        
        return answer
            




















            





        