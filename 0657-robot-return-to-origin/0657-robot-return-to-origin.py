class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        hashMap = {}
        for i in range(len(moves)):
            if moves[i] not in hashMap:
                hashMap[moves[i]] = 1
            else:
                hashMap[moves[i]] += 1

        up = 0
        down = 0
        left = 0
        right = 0

        keys = list(hashMap.keys())
        values = list(hashMap.values())

        for i in range(len(keys)):
            if keys[i] == "U":
                up += values[i]
            if keys[i] == "D":
                down += values[i]
            if keys[i] == "L":
                left += values[i]
            if keys[i] == "R":
                right += values[i]
                
        return up == down and left == right

