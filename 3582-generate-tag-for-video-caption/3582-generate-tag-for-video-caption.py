class Solution:
    def generateTag(self, caption: str) -> str:

        answer = "#"
        for i in range(len(caption)):

            if len(answer) >= 100:
                break

            if caption[i].isalpha() == False:
                continue

            elif caption[i-1] == " ":
                if answer[len(answer)-1] == "#":
                    answer += caption[i].lower()
                    continue
                answer += caption[i].upper()
            else:
                if answer[len(answer)-1] == "#":
                    answer += caption[i].lower()
                    continue
                answer += caption[i].lower()




        return answer
        