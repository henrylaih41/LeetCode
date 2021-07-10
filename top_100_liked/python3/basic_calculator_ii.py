                cur = 0
                op = c
        if(op == "-"):
            stack.append(-cur)
        elif(op == "+"):
            stack.append(cur)
        elif(op == "*"):
            stack.append(stack.pop() * cur)
        elif(op == "/"):
            stack.append(math.trunc(stack.pop() / cur))
        summ = 0
        for s in stack:
            summ += s
        return summ
    ### O(1) space
    def calculate(self, s):
        summ, last, op = 0, 0, "+"
        cur = 0
        for c in s:
            if(c == " "):
                continue
            if(c.isdigit()):
                cur = (cur*10 + int(c))
            else:
                if(op == "+"):
                    summ += last
                    last = cur
                elif(op == "-"):
                    summ += last
                    last = -cur
                elif(op == "*"):
                    last = last * cur
                elif(op == "/"):
                    last = math.trunc(last/cur)
                op = c
                cur = 0
        if(op == "+"):
            summ += last
            last = cur
        elif(op == "-"):
            summ += last
            last = -cur
        elif(op == "*"):
            last = last * cur
        elif(op == "/"):
            last = math.trunc(last/cur)
        summ += last
        return summ
