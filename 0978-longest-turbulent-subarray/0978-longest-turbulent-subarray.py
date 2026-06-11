class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return 1

        def compare(left,right):
            if left > right:    #left bigger
                return -1
            elif left < right:  #right bigger
                return 1
            elif left == right: #same
                return 0
        
        maxLength = 1

        leftPointer = 0

        for rightPointer in range(1,len(arr)):

            curr = compare(arr[rightPointer],arr[rightPointer-1])

            if curr == 0:
                leftPointer = rightPointer
                continue

            if rightPointer == 1:
                maxLength = max(maxLength,rightPointer-leftPointer+1)
                if curr == -1:
                    prev = 1
                else:
                    prev = -1
                continue
            else:
                prev = compare(arr[rightPointer-1],arr[rightPointer-2])

            if curr * prev == -1:
                #good
                maxLength = max(maxLength,rightPointer-leftPointer+1)
            else:
                
                leftPointer = rightPointer-1
                rightPointer = leftPointer+1
                maxLength = max(maxLength,rightPointer-leftPointer+1)


    
        return maxLength

           