class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = min(strs,key=len)
        for i in range(len(base)):
            for j in range(len(strs)):
                if base[i] != strs[j][i]:
                    return base[:i]
        return base