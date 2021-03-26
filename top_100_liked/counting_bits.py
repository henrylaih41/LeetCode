class CountBit:
    def __init__(self):
        self.bits = [0] * 32
        self.count = 0
        
    ### O(n) amortized time complexity 
    def add(self, i):
        if(not self.bits[i]):
            self.bits[i] = 1
            self.count += 1
        else:
            self.bits[i] = 0
            self.count -= 1
            self.add(i+1)
            
class Solution:
    def countBits(self, num: int) -> List[int]:
        bit = CountBit()
        result = [0]
        for i in range(1,num+1):
            bit.add(0)
            result.append(bit.count)
        return result
