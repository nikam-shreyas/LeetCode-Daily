class MyHashMap:

    def __init__(self):
        self.values = [-1 for i in range(1000000)]
        

    def put(self, key: int, value: int) -> None:
        self.values[key%99999] = value

    def get(self, key: int) -> int:
        return self.values[key%99999]
        

    def remove(self, key: int) -> None:
        self.values[key%99999]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)