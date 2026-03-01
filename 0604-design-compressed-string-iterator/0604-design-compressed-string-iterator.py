class StringIterator:

    def __init__(self, compressedString: str):
        self.pointer = -1
        self.string = ""
        pointerOne = 0
        pointerTwo = 0

        while pointerOne < len(compressedString):
            lastChar = compressedString[0]
            frequency = ""
            if compressedString[pointerOne].isnumeric() == False: #Char
                lastChar = compressedString[pointerOne]
                pointerOne+=1
            while pointerOne < len(compressedString) and compressedString[pointerOne].isdigit() == True: #Number
                frequency += compressedString[pointerOne]
                pointerOne+=1
            frequency = int(frequency)
            self.string += (lastChar*frequency)
    
    def next(self) -> str:
        self.pointer += 1
        if self.pointer < len(self.string):
            return self.string[self.pointer]
        else:
            return " "
    
    def hasNext(self) -> bool:
        self.pointer += 1
        if self.pointer < len(self.string):
            self.pointer -= 1
            return True
        else:
            self.pointer -= 1
            return False
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()