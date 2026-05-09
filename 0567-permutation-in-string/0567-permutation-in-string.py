class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        counterOne = Counter(s1)
        counterTwo = Counter()

        k = len(s1)

        for i in range(k):
            if s2[i] not in counterTwo:
                counterTwo[s2[i]] = 1
            else:
                counterTwo[s2[i]] += 1

        if counterOne == counterTwo:
            return True
        
        leftPointer = 0
        rightPointer = k

        answer = False

        while rightPointer <= len(s2)-1:

            if s2[rightPointer] not in counterTwo:
                counterTwo[s2[rightPointer]] = 1
            else:
                counterTwo[s2[rightPointer]] += 1

            counterTwo[s2[leftPointer]] -= 1

            if counterOne == counterTwo:
                answer = True
                break

            leftPointer += 1
            rightPointer +=1

        return answer
