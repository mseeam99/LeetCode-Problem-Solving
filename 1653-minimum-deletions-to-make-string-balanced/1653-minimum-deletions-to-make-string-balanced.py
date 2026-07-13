class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        deletion = 0
        for i in range(len(s)):
            char = s[i]
            if char == "a" and stack and stack[-1] == "b":
                stack.pop()
                deletion += 1
            else:
                stack.append(char)
        return deletion

        