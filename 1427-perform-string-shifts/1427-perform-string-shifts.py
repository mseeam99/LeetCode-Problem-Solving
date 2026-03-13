class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for i in range(len(shift)):
            operation,times = shift[i][0],shift[i][1]
            if operation == 0:
                for j in range(times):
                    s+=s[0]
                    s = s[1:]
            elif operation == 1:
                for j in range(times):
                    s = s[len(s)-1] + s
                    s = s[:len(s)-1]
        return "".join(s)
        