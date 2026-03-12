class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        answer = ""
        count = 0
        for i in range(len(n)-1,-1,-1):
            if count == 3:
                answer += "."
                count = 0
            count += 1 
            answer += n[i]
        return answer[::-1]
        