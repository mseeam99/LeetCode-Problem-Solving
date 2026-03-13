class Solution:
    def reorderSpaces(self, text: str) -> str:

        words = text.split()
        spaceCount = text.count(" ")

        if len(words) == 1:
            return words[0] + " " * spaceCount

        space_between = spaceCount // (len(words) - 1)
        extra_spaces = spaceCount % (len(words) - 1)

        answer = (" " * space_between).join(words)
        answer += " " * extra_spaces

        return answer