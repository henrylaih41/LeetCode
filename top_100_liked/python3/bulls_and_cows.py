class Solution:
    def v2getHint(self, secret: str, guess: str) -> str:
        A, B = 0, 0
        count = defaultdict(lambda: 0)
        skip = set()
        for i in range(len(secret)):
            if(secret[i] == guess[i]):
                A += 1
                skip.add(i)
            else:
                count[secret[i]] += 1
        for i in range(len(secret)):
            if(i in skip):
                continue
            if(count[guess[i]]):
                B += 1
                count[guess[i]] -= 1
        return str(A) + "A" + str(B) + "B"
    
    # one pass
    def getHint(self, secret, guess):
        A, B = 0, 0
        d = defaultdict(lambda: 0)
        for i in range(len(secret)):
            if(secret[i] == guess[i]):
                A += 1
            else:
                B = B + int(d[secret[i]] < 0) + int(d[guess[i]]> 0)
                d[secret[i]] += 1
                d[guess[i]] -= 1
        return str(A) + "A" + str(B) + "B"
​
            
            
