class Solution:
    def intToRoman(self, num: int) -> str:
            d = {
                1:   "I",
                5:   "V",
                10:  "X",
                50:  "L",
                100: "C",
                500: "D",
                1000: "M"
            }
            s, result = [], []
            while(num):
                s.append(num % 10)
                num = num // 10
            i = len(s)-1
            while(len(s)):
                num = s.pop()
                if(num < 4):
                    for _ in range(num):
                        result.append(d[int(10**i)])
                else:
                    if(num == 4):
                        result.append(d[int(10**i)])
                        result.append(d[int(10**(i+1))//2])
                    elif(num >= 5 and num < 9):
                        result.append(d[int(10**(i+1))//2])
                        for _ in range(num - 5):
                            result.append(d[int(10**i)])
                    else:
                        result.append(d[int(10**i)])
                        result.append(d[int(10**(i+1))])
                i -= 1
            return "".join(result)
