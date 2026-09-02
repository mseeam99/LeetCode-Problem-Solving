class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        path = []

        def recursion(start):
            if start == len(s):
                answer.append(path.copy())
                return

            for end in range(start, len(s)):
                substring = s[start:end+1]
                if substring == substring[::-1]:
                    
                    path.append(substring)  # Choose
                    recursion(end+1)          # Process remaining characters
                    path.pop()              # Undo and try another choice

        recursion(0)
        return answer