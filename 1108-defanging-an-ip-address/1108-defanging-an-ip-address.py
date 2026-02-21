class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = ""
        for i in range(len(address)):
            if address[i] != ".":
                answer+=address[i]
            else:
                answer+="[.]"
        return answer
        