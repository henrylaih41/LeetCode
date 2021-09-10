class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if(len(num) < 3):
            return False
        if(num == "".join(['0'] * (len(num)))):
            return True
        for i in range(1, len(num)):
            if(num[0] == "0" and i != 1):
                return False
            for j in range(1, len(num)):
                if(i + j >= len(num)):
                    break
                ### no leading zero
                if(num[i] == "0" and j != 1):
                    break
                seq = []
                seq.append(int(num[:i]))
                seq.append(int(num[i:i+j]))
                if(self.checkValid(seq, num[i+j:])):
                    return True
        return False
                
            
        
    def checkValid(self, sequence, s):
        if(s == ""):
            return False
        i = 0
        while(i < len(s)):
            nxt = sum(sequence)
            cur = 0
            ### no leading zero
            if(s[i] == "0"):
                return False
            while(i < len(s) and cur < nxt):
                cur *= 10
                cur += int(s[i])
                i += 1
            if(i == len(s) and cur == nxt):
                return True
            elif(i < len(s) and cur == nxt):
                sequence.append(cur)
                sequence.pop(0)
