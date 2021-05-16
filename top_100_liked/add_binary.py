class Solution:
    def v1addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a)-1, len(b)-1, 0
        result = []
        while(i >= 0 or j >= 0):
            s1 = 0 if i < 0 else int(a[i])
            s2 = 0 if j < 0 else int(b[j])
            r = (s1 + s2 + carry) % 2
            carry = (s1 + s2 + carry) // 2
            result.append(str(r))
            i -= 1
            j -= 1
        if(carry):
            result.append(str(carry))
        result.reverse()
        return "".join(result)
    
    def addBinary(self, a, b):
        a, b = int(a, 2), int(b, 2)
        x, carry = a ^ b, (a & b) << 1
        while(carry):
            nxt = x ^ carry
            carry = (x & carry) << 1
            x = nxt
        return bin(x)[2:]
