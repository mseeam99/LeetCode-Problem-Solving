class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        another = [1]
        carry = 0
        digitsIndex = len(digits)-1
        anotherIndex = len(another)-1
        answer = []
        while digitsIndex >= 0 or anotherIndex >= 0:

            if digitsIndex >= 0:
                one = digits[digitsIndex]
            else:
                one = 0
            
            if anotherIndex >= 0:
                two = another[anotherIndex]
            else:
                two = 0

            addition = carry + one + two
            answer.append(addition%10)
            carry = addition // 10

            digitsIndex-=1
            anotherIndex-=1

        if carry != 0:
            string = str(carry)
            for i in range(len(string)):
                answer.append(int(string[i]))

        return answer[::-1]






            

            

    