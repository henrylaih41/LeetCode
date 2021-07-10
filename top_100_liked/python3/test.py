from typing import List
from functools import wraps
from time import time

def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
    return _time_it

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

@measure
def countBits(num: int) -> List[int]:
    bit = CountBit()
    result = [0]
    for i in range(1,num+1):
        bit.add(0)
        result.append(bit.count)
    return result
test = [1e4, 1e5, 1e6, 1e7]
@measure
def loop(num):
    count = 0
    for i in range(num):
        count += 1
#loop(int(1e8))
for i in test:
    countBits(int(i))
