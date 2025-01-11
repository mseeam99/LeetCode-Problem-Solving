import itertools

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        answer = set()
        
        for length in range(1, len(tiles) + 1):
            for perm in itertools.permutations(tiles, length):
                answer.add(perm)
        
        return len(answer)
