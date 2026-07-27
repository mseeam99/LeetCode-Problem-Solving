class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        for i in range(1,len(colors)-1):
            if colors[i-1] == "A" and colors[i] == "A" and colors[i+1] == "A":
                a += 1
            elif colors[i-1] == "B" and colors[i] == "B" and colors[i+1] == "B":
                b += 1
        if a > b:
            return True
        else:
            return False