class Solution:
    def reformatDate(self, date: str) -> str:

        hashMap = {}
        hashMap["Jan"] = "01"
        hashMap["Feb"] = "02"
        hashMap["Mar"] = "03"
        hashMap["Apr"] = "04"
        hashMap["May"] = "05"
        hashMap["Jun"] = "06"
        hashMap["Jul"] = "07"
        hashMap["Aug"] = "08"
        hashMap["Sep"] = "09"
        hashMap["Oct"] = "10"
        hashMap["Nov"] = "11"
        hashMap["Dec"] = "12"

        answer = ""
        array = date.split(" ")
        for i in range(len(array)-1,-1,-1):
            if i == 2:
                answer += array[i]
                answer += "-"
            elif i == 1:
                answer += hashMap[str(array[i])]
                answer += "-"
            elif i == 0:
                s = ""
                currentString = array[0]
                for j in range(len(currentString)):
                    if currentString[j].isnumeric():
                        s+=currentString[j]
                if len(s)==2:
                    answer += s
                else:
                    p = "0"+s
                    answer += p
        return answer

        
       

        