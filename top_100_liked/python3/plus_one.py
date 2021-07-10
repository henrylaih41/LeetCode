class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        self.overflow = 0
        self.plus(digits, len(digits)-1)
        ### if not overflow
        if(not self.overflow):
            return digits
        ### if overflow
        n = [1]
        for d in digits:
            n.append(d)
        return n
        
    def plus(self, digits, i):
        if(digits[i] == 9):
            digits[i] = 0
            if(i == 0):
                self.overflow = 1
                return
            self.plus(digits, i-1)
        else:
            digits[i] += 1
