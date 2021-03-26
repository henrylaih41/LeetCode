class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        s = []
        for i in range(len(T)):
            while(len(s) != 0 and T[i] > T[s[-1]]):
                j = s.pop()
                result[j] = i - j
            s.append(i)
        return result
        
