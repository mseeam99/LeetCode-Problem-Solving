class Solution:
    def largestOddNumber(self, num: str) -> str:


        rightPointer = len(num)-1

        while rightPointer >= 0:
            if int(num[rightPointer]) % 2 != 0:
                break

            rightPointer -= 1

        return num[:rightPointer+1]
            


        
                

                


        