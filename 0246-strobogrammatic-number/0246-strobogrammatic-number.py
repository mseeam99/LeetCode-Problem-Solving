class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        hashMap = {}

        for i in range(10):
            if i == 0:
                hashMap[i] = 0
            elif i == 1:
                hashMap[i] = 1
            elif i == 6:
                hashMap[i] = 9
            elif i == 8:
                hashMap[i] = 8
            elif i == 9:
                hashMap[i] = 6
            else:
               hashMap[i] = "BAD"
        

        answer = ""
        for i in range(len(num)):
            if hashMap[int(num[i])] == "BAD":
                return False
            else:
                answer += str(hashMap[int(num[i])])
        print(answer)

        return True if answer[::-1] == num else False

        