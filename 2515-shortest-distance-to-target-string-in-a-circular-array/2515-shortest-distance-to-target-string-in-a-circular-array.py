class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:

        closest = float("inf")
        rightDistance = float("inf")
        leftDistance = float("inf")

        for i in range(len(words)):

            if words[i] == target:
                rightDistance = abs(min(rightDistance, i - startIndex))
                rightDistance = abs(min(rightDistance, abs(len(words)-i)+startIndex))
                leftDistance  = abs(min(leftDistance, startIndex-i))
                leftDistance  = abs(min(leftDistance, abs(i+len(words)-startIndex)))
                closest = min(closest, rightDistance, leftDistance)

        return -1 if closest == float("inf") else closest