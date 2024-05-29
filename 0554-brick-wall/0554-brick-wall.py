class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        hashMap = {}

        for row in range(len(wall)):
            total = 0
            for brick in range(len(wall[row]) - 1):
                total += wall[row][brick]
                hashMap[total] = 1 + hashMap.get(total, 0)

        if not hashMap:
            return len(wall)

        answer = len(wall) - max(hashMap.values())
        return answer


        