class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashMap = {i: chr(96 + i) for i in range(1, 27)}

        res = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])     
                res.append(hashMap[num])
                i -= 3
            else:
                num = int(s[i])        
                res.append(hashMap[num])
                i -= 1

        return "".join(res[::-1])