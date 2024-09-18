class Logger:

    def __init__(self):
        self.hashMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hashMap:
            self.hashMap[message] = timestamp + 10
            return True
        else:
            timeLimit = self.hashMap[message]
            if timestamp >= timeLimit:
                self.hashMap[message] = timestamp + 10
                return True
            else:
                return False
                
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)