class Solution:
    def intToRoman(self, num: int) -> str:
        theList = [
            [1000,"M"],
            [900,"CM"],
            [500,"D"],
            [400,"CD"],
            [100,"C"],
            [90,"XC"],
            [50,"L"],
            [40,"XL"],
            [10,"X"],
            [9,"IX"],
            [5,"V"],
            [4,"IV"],
            [1,"I"]
        ]
        answer = ""
        for i in range(len(theList)):
            val, sym = theList[i][0],theList[i][1]
            while num >= val:
                answer += sym
                num = num - val
        return answer