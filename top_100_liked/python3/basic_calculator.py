class Solution:
    def calculate(self, s: str) -> int:
        i, sign = 0, 1
        st = []
        while(i < len(s)):
            if(s[i].isdigit()):
                num, ni = self.getNumber(s, i)
                st.append(sign * num)
                i = ni
            else:
                if(s[i] == "-"):
                    sign = -1
                elif(s[i] == "+"):
                    sign = 1
                elif(s[i] == "("):
                    st.append(sign)
                    st.append("(")
                    sign = 1
                elif(s[i] == ")"):
                    summ = 0
                    while(st[-1] != "("):
                        summ += st.pop()
                    st.pop()
                    st.append(st.pop() * summ)
                    sign = 1
                i += 1
        return sum(st)
    
    ### get number starting from s[i]
    def getNumber(self, s, i):
        summ = 0
        while(i < len(s) and s[i].isdigit()):
            summ *= 10
            summ += int(s[i])
            i += 1
