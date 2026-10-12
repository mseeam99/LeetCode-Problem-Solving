class MyHashSet:
    def __init__(self):
        self.hashValue = 1000
        self.bucket = []
        for i in range(self.hashValue+1):
            self.bucket.append([])

    def add(self, key: int) -> None:
        index = key % self.hashValue
        if self.contains(key) == False:
            self.bucket[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.hashValue
        if key in self.bucket[index]:
            self.bucket[index].remove(key)
            
    def contains(self, key: int) -> bool:
        index = key % self.hashValue
        doContain = False
        for i in range(len(self.bucket[index])):
            if self.bucket[index][i] == key:
                doContain = True
                break
        return doContain

    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)