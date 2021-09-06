class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        vectors = [v1, v2]
        self.curr = 0
        self.lists = []
        self.valid = []
        self.pos = []
        for v in vectors:
            if(len(v) == 0):
                continue
            self.valid.append(len(self.lists))
            self.lists.append(v)
            self.pos.append(0)
        
    def next(self) -> int:
        list_idx = self.valid[self.curr]
        val = self.lists[list_idx][self.pos[list_idx]]
        self.pos[list_idx] += 1
        if(self.pos[list_idx] == len(self.lists[list_idx])):
            self.valid.remove(list_idx)
            if(self.curr == len(self.valid)):
                self.curr = 0
            ### after remove curr would point to the next valid list
        elif(len(self.valid)):
            self.curr = (self.curr + 1) % len(self.valid)
        else:
            self.curr = None
        return val
    def hasNext(self) -> bool:
        return len(self.valid)
​
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
