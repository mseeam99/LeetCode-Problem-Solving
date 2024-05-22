class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.hashMap = [[] for _ in range(self.size)]
        
    def put(self, key: int, value: int) -> None:
        bucket = key % self.size
        for i, (k, v) in enumerate(self.hashMap[bucket]):
            if k == key:
                self.hashMap[bucket][i] = (key, value)
                return
        self.hashMap[bucket].append((key, value))
        
    def get(self, key: int) -> int:
        bucket = key % self.size
        for k, v in self.hashMap[bucket]:
            if k == key:
                return v
        return -1
        
    def remove(self, key: int) -> None:
        bucket = key % self.size
        for i, (k, v) in enumerate(self.hashMap[bucket]):
            if k == key:
                del self.hashMap[bucket][i]
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
