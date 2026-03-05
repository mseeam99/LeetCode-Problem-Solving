class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowels = set(["a", "e", "i", "o", "u"])
        returnCount = 0

        for i in range(len(word)):
            seen = set()
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break
                else:
                    seen.add(word[j])
                    if len(seen) >= 5:
                        returnCount += 1

        return returnCount