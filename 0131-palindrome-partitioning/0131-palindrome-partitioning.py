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
                    
                    path.append(substring)
                    recursion(end+1)
                    path.pop()

        recursion(0)
        return answer