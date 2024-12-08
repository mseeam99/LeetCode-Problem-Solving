class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newString = [""] * len(s)
        for i in range(len(indices)):
            newString[indices[i]] = s[i]
        return "".join(newString)
