class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binarySearch(array):
            left = 0
            right = len(array)-1
            while left <= right:
                middle = left + (right-left) // 2
                if array[middle] == 0:
                    right = middle - 1 
                else:
                    left = middle + 1
            return left

        myQueue = []
        for i in range(len(mat)):
            oneCount = binarySearch(mat[i])
            myQueue.append([oneCount,i])

        myQueue.sort()
        answer = []
        for i in range(k):
            answer.append(myQueue[i][1])
        return answer
        


        