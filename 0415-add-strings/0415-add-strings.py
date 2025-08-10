class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        answer = ""
        carry = 0

        length1 = len(num1)-1
        length2 = len(num2)-1

        while length1 >= 0 or length2 >= 0:
            
            if length1 >= 0:
                digitOne = int(num1[length1])
            else:
                digitOne = 0

            if length2 >= 0:
                digitTwo = int(num2[length2])
            else:
                digitTwo = 0

            addition = digitOne + digitTwo + carry
            carry = addition // 10
            remainder = addition % 10

            answer+=str(remainder)
            length1-=1
            length2-=1
        
        if carry:
            answer+=str(carry)

        return answer[::-1]









        