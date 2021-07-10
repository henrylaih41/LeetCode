class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.num, self.target = num, target
        self.result = []
        #self.brute([num[0]], 1, int(num[0]))
        self.dfs([num[0]], 1, int(num[0]), int(num[0]), int(num[0]))
        return self.result
    
    ### brute, calculate val at the end
    def brute(self, ss, i, operand):
        if(i >= len(self.num)):
            exp = "".join(ss)
            if(eval(exp) == self.target):
                self.result.append(exp)
            return
        
        for op in "+-* ":
            if(op == " " and operand):
                ss.append(self.num[i])
                self.brute(ss, i+1, operand*10 + int(self.num[i]))
                ss.pop()
            elif(op != " "):
                ss.append(op)
                ss.append(self.num[i])
                self.brute(ss, i+1, int(self.num[i]))
                ss.pop()
                ss.pop()
            
    def dfs(self, ss, i, operand, value, last_add):
