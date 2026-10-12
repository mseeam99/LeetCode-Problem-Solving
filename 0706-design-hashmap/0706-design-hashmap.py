class MyHashMap:
    def __init__(self):
        self.hashValue = 500
        self.array = []
        for i in range(self.hashValue+1):
            self.array.append([])

    def put(self, key: int, value: int) -> None:
        index = key % self.hashValue 
        if len(self.array[index]) > 0:
            found = False
            for i in range(len(self.array[index])):
                if self.array[index][i][0] == key:
                    self.array[index][i][1] = value
                    found = True
                    break
            if found == False:
                self.array[index].append([key,value])
        else:
            self.array[index].append([key,value])

    def get(self, key: int) -> int:
        index = key % self.hashValue 
        if len(self.array[index]) > 0:
            for i in range(len(self.array[index])):
                pair = self.array[index][i]
                if pair[0] == key:
                    return pair[1]
        return -1
        
    def remove(self, key: int) -> None:
        idx = 0
        exist = False
        index = key % self.hashValue 
        if len(self.array[index]) > 0:
            for i in range(len(self.array[index])):
                pair = self.array[index][i]
                if pair[0] == key:
                    idx = i
                    exist = True
                    break
            if exist == True:
                self.array[index] = self.array[index][:idx] + self.array[index][idx+1:]
        else:
            return None
        
                            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)