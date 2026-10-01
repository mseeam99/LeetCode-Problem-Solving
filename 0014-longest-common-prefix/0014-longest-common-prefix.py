class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        res = ""

        for i in range(len(strs[0])):
            for w in range(1,len(strs)):
                word = strs[w]
                if i >= len(word) or word[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res








        