class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        outerdp = [0] * (len(text2) + 1)
        for i in range(len(text1)):
            innerdp = [0] * (len(text2) + 1)
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    innerdp[j+1] = outerdp[j] + 1
                else:
                    innerdp[j+1] = max(innerdp[j],outerdp[j+1])
            outerdp = innerdp
        return outerdp[-1]



        