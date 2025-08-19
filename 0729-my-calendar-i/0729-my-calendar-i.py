class MyCalendar:

    def __init__(self):
        self.array = []

    def binarySearch(self, target, array):    
        left = 0
        right = len(array)
        while left < right:
            middle = left + (right - left) // 2 
            if array[middle][1] == target:
                return (middle,"EXIST")
            if target > array[middle][1]:
                left = middle + 1
                continue
            if target < array[middle][1]:
                right = middle 
                continue
            left += 1
        return (left,"NOTEXIST")

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.array) == 0:
            self.array.append([startTime,endTime])
            return True
        else:
            copy = self.array.copy()
            self.array.append([startTime,endTime])
            self.array.sort()
            for i in range(1,len(self.array)):
                if self.array[i][0] < self.array[i-1][1]:
                    self.array = copy
                    return False
            return True
