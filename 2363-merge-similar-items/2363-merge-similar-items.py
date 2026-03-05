class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        for i in range(len(items2)):
            items1.append(items2[i])
        items1.sort()
        print(items1)

        answer = []

        pointerLeft = 0
        pointerRight = 0
        
        while pointerLeft <= len(items1)-1 and pointerRight <= len(items1)-1:
            while pointerRight <= len(items1)-1 and items1[pointerLeft][0] == items1[pointerRight][0]:
                pointerRight += 1
            if pointerLeft+1 != pointerRight:
                value = [items1[pointerLeft][0],items1[pointerLeft][1]+items1[pointerRight-1][1]]
                answer.append(value)
            else:
                answer.append(items1[pointerLeft])
            pointerLeft = pointerRight

       


        return answer
        



        


        

        

     


        