class Solution:
    def myAtoi(self, s: str) -> int:
        sign, summ = 1, 0
        st = []
        if(len(s) == 0):
            return summ
        i = 0
        while(i < len(s) and s[i] == " "):
            i += 1
        if(i < len(s) and s[i] in "-+"):
            if(s[i] == "-"):
                sign = -1
            i += 1
        poww = 1
        while(i < len(s) and s[i].isdigit()):
            st.append(s[i])
            i += 1
        while(len(st) != 0):
            i = st.pop()
            summ += poww * self.toInt(i)
            poww *= 10
        summ *= sign
        if(summ > (1 << 31) - 1):
            summ = (1 << 31) - 1
        if(summ < -(1 << 31)):
            summ = -(1 << 31)
        
        return summ
    def toInt(self, c):
        return ord(c) - ord('0')
