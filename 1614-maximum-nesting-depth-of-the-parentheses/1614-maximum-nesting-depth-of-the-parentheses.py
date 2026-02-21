class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDepth = 0
        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
                maxDepth = max(maxDepth, depth)
            elif s[i] == ")":
                depth -= 1
        return maxDepth
        