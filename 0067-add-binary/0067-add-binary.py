class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        i = len(a)-1
        j = len(b)-1
        for _ in range(max(len(a),len(b))):
            aDigit = int(a[i]) if i >= 0 else 0 
            bDigit = int(b[j]) if j >= 0 else 0 
            summation = aDigit + bDigit + carry
            result = str(summation % 2) + result
            carry = summation // 2
            i-=1
            j-=1
        if carry:
            result = str(carry) + result
        return result


        