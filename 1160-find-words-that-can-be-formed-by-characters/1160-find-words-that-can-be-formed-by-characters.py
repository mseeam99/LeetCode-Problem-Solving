class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        answer = 0
        for i in range(len(words)):
            counter = Counter(chars)
            goodFound = True
            for j in range(len(words[i])):
                if words[i][j] in counter and counter[words[i][j]] > 0:
                    counter[words[i][j]] -= 1
                    continue
                elif words[i][j] not in counter or counter[words[i][j]] <= 0:
                    goodFound = False
                    break
            if goodFound == True:
                answer += len(words[i])
        return answer