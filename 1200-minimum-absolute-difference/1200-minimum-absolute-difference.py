class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()

        minimumDifference = arr[1]-arr[0]
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                minimumDifference = min(minimumDifference,abs(arr[i+1]-arr[i]))

        answer = []
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                if abs(arr[i+1]-arr[i]) == minimumDifference:
                    answer.append([arr[i],arr[i+1]])
        return answer

        