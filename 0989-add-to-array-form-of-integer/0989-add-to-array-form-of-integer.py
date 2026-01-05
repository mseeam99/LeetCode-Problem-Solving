class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        top = num
        k = str(k)
        bottom = [0] * len(str(k))
        for i in range(len(str(k))):
            bottom[i] = int(k[i])
        topIndex = len(top)-1
        bottomIndex = len(bottom)-1
        answer = []
        carry = 0
       
        while topIndex >= 0 or bottomIndex >= 0:
            
            if topIndex >= 0: 
                topValue = top[topIndex]
            else:
                topValue = 0
            
            if bottomIndex >= 0: 
                bottomValue = bottom[bottomIndex]
            else:
                bottomValue = 0

            addition = topValue + bottomValue + carry
            answer.append(addition % 10)
            carry = addition // 10
        
            topIndex-=1
            bottomIndex-=1

        if carry != 0:
            s = str(carry)    
            for i in range(len(s)):
                answer.append(int(s[i]))

        return answer[::-1]

            
       

        