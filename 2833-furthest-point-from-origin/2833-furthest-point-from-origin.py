class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        _count = 0
        Lcount = 0
        Rcount = 0

        for i in range(len(moves)):
            if moves[i] == "L":
                Lcount += 1
            elif moves[i] == "R":
                Rcount += 1
            else:
                _count += 1

        return abs(Rcount-Lcount)+_count








        