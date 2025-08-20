class MyCalendarTwo:

    def __init__(self):
        self.hashMap = {}
        self.count = 0

    def book(self, startTime: int, endTime: int) -> bool:

        if startTime not in self.hashMap:
            self.hashMap[startTime] = 1
        else:
            self.hashMap[startTime] += 1
        
        if endTime not in self.hashMap:
            self.hashMap[endTime] = -1
        else:
            self.hashMap[endTime] -= 1


        for key,val in sorted(self.hashMap.items()):

            self.count += val

            if self.count >= 3:

                if self.hashMap[startTime] == 1:
                    del self.hashMap[startTime]
                else:
                    self.hashMap[startTime] -= 1

                if self.hashMap[endTime] == -1:
                    del self.hashMap[endTime]
                else:
                    self.hashMap[endTime] += 1
                self.count = 0
                return False
                
        self.count = 0
        return True 

            
                
        











        
        

