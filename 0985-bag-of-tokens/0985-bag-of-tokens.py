class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        max_score = 0
        leftPointer  = 0
        rightPointer = len(tokens) - 1

        while leftPointer <= rightPointer:
            if power >= tokens[leftPointer]:
                power -= tokens[leftPointer]
                score += 1
                leftPointer += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[rightPointer]
                score -= 1
                rightPointer -= 1
            else:
                break
        return max_score


