class Solution:
    def countOddLetters(self, n: int) -> int:

        n = str(n)
        hashMap = {}
        hashMap["0"] = "zero"
        hashMap["1"] = "one"
        hashMap["2"] = "two"
        hashMap["3"] = "three"
        hashMap["4"] = "four"
        hashMap["5"] = "five"
        hashMap["6"] = "six"
        hashMap["7"] = "seven"
        hashMap["8"] = "eight"
        hashMap["9"] = "nine"
        string = ""

        

        for i in range(len(n)):
            if n[i] in hashMap:
                string += hashMap[n[i]]

        print(string)

        counter = Counter(string)
        print(counter)

        answer = 0

        for key,val in counter.items():
            if int(val) % 2 != 0:
                answer += 1
        
        return answer





        