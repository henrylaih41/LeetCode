import math
class Solution:
    def calculate(self, s: str) -> int:
        stack, curr, op = [], 0, "+"
        
        for c in s:
            if(c.isdigit()):
                curr = (curr*10 + int(c))
                continue
            if(c == "("):
                stack.append(op)
                stack.append("(")
                op = "+"
                continue
            if(op == "+"):
                stack.append(curr)
            if(op == "-"):
                stack.append(-curr)
            if(op == "*"):
                stack.append(stack.pop() * curr)
            if(op == "/"):
                stack.append(math.trunc(stack.pop() / curr))
            curr = 0
            op = c
            if(c == ")"):
                summ = 0
                while(stack[-1] != "("):
                    summ += stack.pop()
                stack.pop()
                op = stack.pop()
                if(op == "+"):
                    stack.append(summ)
