class Solution:
    def __init__(self):
        self.ops = {
            "-" : operator.sub,
            "+" : operator.add,
            "*" : operator.mul
        }   
        self.memo = {}
        
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if(expression.isnumeric()):
            return [int(expression)]
        if(expression in self.memo):
            return self.memo[expression]
        s = []
        for i in range(len(expression)):
            if(expression[i] in "-+*"):
                for l in self.diffWaysToCompute(expression[:i]):
                    for r in self.diffWaysToCompute(expression[i+1:]):
                        s.append(self.ops[expression[i]](l, r))
        self.memo[expression] = s
        return s
