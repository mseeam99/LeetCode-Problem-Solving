class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        visited = set()
        queue = [0]
        farthest = 0

        while queue:
            pointer = queue.pop(0)

            start = max(pointer + minJump, farthest + 1)
            end = min(pointer + maxJump + 1, n)

            for i in range(start, end):
                if s[i] == '0' and i not in visited:
                    if i == n - 1:
                        return True
                    queue.append(i)
                    visited.add(i)

            farthest = max(farthest, pointer + maxJump)

        return n - 1 in visited
