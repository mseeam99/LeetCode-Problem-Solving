class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        last = colors[0]
        l = 0
        colors.extend(colors[:k-1])
        t = 0
        for c in colors:
            if c == last:
                l = 1
            else:
                l += 1
                last = c
                if l >= k:
                    t += 1
        return t