class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        if s[-1] != "0":
            return False

        queue = deque([0])
        farthestChecked = 0

        while queue:

            currentIndex = queue.popleft()

            leftPointer = max(currentIndex + minJump, farthestChecked + 1)
            rightPointer = min(currentIndex + maxJump, len(s) - 1)

            for nextIndex in range(leftPointer, rightPointer + 1):
                if s[nextIndex] == "0":
                    queue.append(nextIndex)

                    if nextIndex == len(s) - 1:
                        return True

            farthestChecked = max(farthestChecked, rightPointer)

        return False