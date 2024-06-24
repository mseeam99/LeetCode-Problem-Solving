class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        pointerOne = 0
        pointerTwo = 0
        count      = 0

        while pointerOne < len(g) and pointerTwo < len(s):
            if s[pointerTwo] >= g[pointerOne]:
                count+=1
                pointerOne+=1
                pointerTwo+=1
            else:
                pointerTwo+=1
            
        return count


        