class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        depth = 0
        for i in range(len(s)):
            if s[i] == "(":
                if depth > 0:
                    stack.append(s[i])
                depth += 1
            elif s[i] == ")":
                depth -= 1
                if depth > 0:
                    stack.append(s[i])
        return "".join(stack)


        