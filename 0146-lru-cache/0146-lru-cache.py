class LRUCache:

    def __init__(self, capacity: int):
        self.l = []
        self.d = {}
        self.count = capacity
    
    def get(self, key: int) -> int:
        if self.d.get(key) is not None:
            self.l.remove(key)
            self.l.append(key)
            return self.d[key]     
        return -1
        
    def put(self, key: int, value: int) -> None:
        if self.d.get(key) is not None:
            self.d[key] = value
            self.l.remove(key)
            self.l.append(key)
        elif len(self.l)<self.count:
            self.l.append(key)
            self.d[key] = value
        else:
            a = self.l.pop(0)
            del self.d[a]
            self.l.append(key)
            self.d[key] = value