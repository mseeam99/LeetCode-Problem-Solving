class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points = 0
        stack = []
        if x > y:
            for i in range(len(s)):
                if stack and stack[-1] == "a" and s[i] == "b":
                    stack.pop()
                    points += x
                else:
                    stack.append(s[i])
            s = ""
            for i in range(len(stack)):
                s += stack[i]
            stack.clear()
            for i in range(len(s)):
                if stack and stack[-1] == "b" and s[i] == "a":
                    stack.pop()
                    points += y
                else:
                    stack.append(s[i])
        else:
            for i in range(len(s)):
                if stack and stack[-1] == "b" and s[i] == "a":
                    stack.pop()
                    points += y
                else:
                    stack.append(s[i])
            s = ""
            for i in range(len(stack)):
                s += stack[i]
            stack.clear()
            for i in range(len(s)):
                if stack and stack[-1] == "a" and s[i] == "b":
                    stack.pop()
                    points += x
                else:
                    stack.append(s[i])
        return points

        
        