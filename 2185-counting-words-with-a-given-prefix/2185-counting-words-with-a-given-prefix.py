class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in range(len(words)):
            currentWord = words[i]
            if len(currentWord) >= len(pref):
                for j in range(len(pref)):
                    if pref[j] != currentWord[j]:
                        break
                    if j == len(pref)-1:
                        count += 1
        return count

        