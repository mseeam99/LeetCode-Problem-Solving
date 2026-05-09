class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        colors.extend(colors[:k - 1])

        lastColor = colors[0]

        alternatingLength = 1
        count = 0

        for i in range(1, len(colors)):

            currentColor = colors[i]

            if currentColor == lastColor:
                alternatingLength = 1
            else:
                alternatingLength += 1

            lastColor = currentColor

            if alternatingLength >= k:
                count += 1

        return count