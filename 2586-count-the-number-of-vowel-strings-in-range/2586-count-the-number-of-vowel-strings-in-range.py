class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        count = 0
        for i in range(left,right+1):
            if words[i][0] == "a" or words[i][0] == "e" or words[i][0] == "i" or words[i][0] == "o" or words[i][0] == "u":
                if words[i][-1] == "a" or words[i][-1] == "e" or words[i][-1] == "i" or words[i][-1] == "o" or words[i][-1] == "u":
                    count += 1
        return count 
        