class Solution:
    def balancedStringSplit(self, s: str) -> int:


        rightPointer = 0

        count = 0

        rcount = 0
        lcount = 0

        while rightPointer <= len(s)-1:
            if s[rightPointer] == "R":
                rcount += 1
            elif s[rightPointer] == "L":
                lcount += 1

            if rcount == lcount:
                count += 1
                rcount = 0
                lcount = 0


            rightPointer += 1

            

            


        
        return count



        