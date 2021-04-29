class Vector2D:
​
    def __init__(self, vec: List[List[int]]):
        self.len, self.count, self.vec = 0, 0, vec
        for l in vec:
            for c in l:
                self.len += 1
        self.gen = self.generator()
        
    def next(self) -> int:
        self.count += 1
        return next(self.gen)
    
    def generator(self):
        for l in self.vec:
            for c in l:
                yield c
    
    def hasNext(self) -> bool:
        if(self.count >= self.len):
            return False
        return True
​
# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
