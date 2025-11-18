class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        if len(grades) == 1:
            return 1

        grades.sort()
        print(grades) 
        
        def linearIterCheck(group):
            if (group * (group + 1) / 2) <= len(grades):
                return True
            return False

        left = 0
        right = len(grades)-1
        groupNumber = 0
        while left <= right:
            middle = left + (right-left) // 2
            if linearIterCheck(middle) == True:
                left = middle + 1
                groupNumber = middle
            else:
                right = middle - 1
        return groupNumber