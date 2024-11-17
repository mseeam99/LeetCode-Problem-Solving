class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelAsString = "aeiouAEIOU"
        vowels = ""
        for i in range(len(s)):
            if s[i] in vowelAsString:
                vowels+=s[i]
        newvowels = list(vowels[::-1])
        index = 0
        answer = ""
        for i in range(len(s)):
            if s[i] in vowelAsString:
                answer += newvowels[index]
                index+=1
            else:
                answer += s[i]
        return answer


        

        