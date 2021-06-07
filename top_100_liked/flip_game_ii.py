class Solution:
    def canWin(self, currentState: str) -> bool:
        arr, count = [0], 0
        for i in range(len(currentState)-1):
            if(currentState[i] == "+" and currentState[i+1] == "+"):
                arr.append(1)
                count += 1
            else:
                arr.append(0)
        arr.append(0)
        return self.recur(arr, count)
    
    def recur(self, arr, count):
        ### must lose
        if(count == 0):
            return 0
        ### must win
        if(count == 1):
            return 1
        flag = 0
        for i in range(1, len(arr)-1):
            if(arr[i] == 1):
                old = [arr[i-1], arr[i], arr[i+1]]
                arr[i-1], arr[i], arr[i+1] = 0, 0, 0
                count -= sum(old)
                if(not self.recur(arr, count)):
                    flag = 1
                arr[i-1], arr[i], arr[i+1] = old
                count += sum(old)
                if(flag):
