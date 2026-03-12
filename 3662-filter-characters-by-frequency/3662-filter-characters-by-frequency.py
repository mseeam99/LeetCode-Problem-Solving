class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        hashMap = Counter(s)
        answer = ""
        for i in range(len(s)):
            if hashMap[s[i]] < k:
                answer += s[i]
        return answer   