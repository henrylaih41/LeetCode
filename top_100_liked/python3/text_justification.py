class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, tmp = [], []
        i, ll = 0, 0
        while(i < len(words)):
            tmp.append(words[i])
            ll += len(words[i])
            if(ll + len(tmp) - 1 > maxWidth):
                ll -= len(tmp[-1])
                tmp.pop()
                spaces = self.spaces(maxWidth - ll, len(tmp)-1)
                for j in range(len(tmp)):
                    tmp[j] = tmp[j] + (" " * spaces[j])
                result.append("".join(tmp))
                tmp, ll = [], 0
            else:
                i += 1
        
        if(len(tmp)):
            for j in range(len(tmp)-1):
                tmp[j] = tmp[j] + " "
            tmp.append(" " * (maxWidth - ll - len(tmp) + 1))
            result.append("".join(tmp))
        return result
    
    def spaces(self, n, k):
        if(k == 0):
            return [n]
        result = [n // k] * k
        for i in range(n % k):
            result[i] += 1
        result.append(0)
        return result
