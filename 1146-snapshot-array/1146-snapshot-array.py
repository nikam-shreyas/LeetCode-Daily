class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = -1
        self.snaps = []
        self.changes = {}

    def set(self, index: int, val: int) -> None:
        # print('set', self.snaps,  self.changes)
        self.changes[index]=val

    def snap(self) -> int:
        # print('snap', self.snaps,  self.changes)
        self.snap_id+=1
        self.snaps.append(self.changes.copy())
        self.changes = {}
        return self.snap_id
        

    def get(self, index: int, snap_id: int) -> int:
        # print('get', self.snaps,  self.changes)
        while snap_id>=0:
            if index in self.snaps[snap_id]:
                return self.snaps[snap_id][index]
            snap_id-=1
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)