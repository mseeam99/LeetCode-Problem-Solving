class MyCalendar:

    def __init__(self):
        self.array = []

    def bisectLeft(self, target):    
        left, right = 0, len(self.array)
        while left < right:
            mid = (left + right) // 2
            if self.array[mid][0] < target:
                left = mid + 1
            else:
                right = mid
        return left 

    def book(self, startTime: int, endTime: int) -> bool:

        if len(self.array) == 0:
            self.array.append([startTime,endTime])
            return True

        else:

            i = self.bisectLeft(startTime)
            
            if i > 0 and self.array[i - 1][1] > startTime:
                return False

            if i < len(self.array) and i <= len(self.array)-1 and endTime > self.array[i][0]:
                return False
           
            self.array.insert(i, [startTime, endTime])

            return True

