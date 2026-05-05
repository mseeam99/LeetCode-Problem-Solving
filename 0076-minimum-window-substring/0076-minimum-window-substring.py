class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hashMap = {}
        for i in range(len(t)):
            if t[i] not in hashMap:
                hashMap[t[i]] = 1
            else:
                hashMap[t[i]] += 1
        
        leftPointer = 0
        rightPointer = 0
        biggerHashMap = {}
        minLength = float("inf")
        answer = ""

        while rightPointer <= len(s)-1:

            if s[rightPointer] not in biggerHashMap:
                biggerHashMap[s[rightPointer]] = 1
            else:
                biggerHashMap[s[rightPointer]] += 1
            
            # now to check if biggerHashMap has >= elements of hashMap
            boolean = True
            while boolean == True:
                for key,val in hashMap.items():
                    if key in biggerHashMap and biggerHashMap[key] >= val:
                        continue
                    else:
                        boolean = False
                        break

                if boolean == True:
                    windowLength = rightPointer - leftPointer + 1
                    if windowLength <= minLength:
                        minLength = min(minLength,windowLength)
                        answer = s[leftPointer:rightPointer + 1]

                    biggerHashMap[s[leftPointer]] -= 1
                    if biggerHashMap[s[leftPointer]] == 0:
                        del biggerHashMap[s[leftPointer]]
                    leftPointer += 1
            rightPointer += 1

        return answer





        
            




        