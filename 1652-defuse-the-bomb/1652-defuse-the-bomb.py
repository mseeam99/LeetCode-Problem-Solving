class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        if k == 0:
            return [0]*len(code)
        answerArray = [0]*len(code)
        if k > 0:
            summation = 0
            for i in range(k):
                summation += code[i]
            for i in range(len(code)):
                summation += code[((i+k)%len(code))]
                summation -= code[i]
                answerArray[i] = summation
        else:
            k = abs(k)
            summation = 0
            for i in range(1, k + 1):
                summation += code[-i]
            for i in range(len(code)):
                answerArray[i] = summation
                summation -= code[(i - k) % len(code)]
                summation += code[i % len(code)]
        return answerArray


        
        