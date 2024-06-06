class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        myString = ""
        count = 0

        # First pass to remove invalid right parentheses ")"
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            elif s[i] == ")":
                if count == 0:
                    continue
                else:
                    count -= 1
            myString += s[i]

        answer = ""
        count = 0  # Reset count for the second pass

        # Second pass to remove invalid left parentheses "(" from the right
        for i in range(len(myString) - 1, -1, -1):
            if myString[i] == ")":
                count += 1
            elif myString[i] == "(":
                if count == 0:
                    continue
                else:
                    count -= 1
            answer += myString[i]

        # Reverse the answer to correct the order
        answer = answer[::-1]

        return answer


