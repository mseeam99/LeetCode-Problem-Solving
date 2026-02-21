class Solution:
    def maxDepth(self, s: str) -> int:
        
        depth = 0
        stack = []
        maxDepth = 0
       

        for i in range(len(s)):

            if s[i] == "(":
                depth += 1
                maxDepth = max(maxDepth, depth)
                stack.append(s[i])
            elif s[i] == ")":
                depth -= 1
        
        return maxDepth
        