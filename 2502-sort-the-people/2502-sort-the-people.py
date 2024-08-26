class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        answer = []
        hashMap = {}

        for i in range(len(heights)):
            hashMap[heights[i]] = names[i]

        heights.sort()
        heights = heights[::-1]

        for i in range(len(heights)):
            answer.append(hashMap[heights[i]])

        return answer

        

        


        