class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if(numerator == 0):
            return "0"
        result = []
        sign1, sign2 = numerator/abs(numerator), denominator/abs(denominator)
        numerator, denominator = abs(numerator), abs(denominator)
        result.append(str(numerator // denominator)) # integer part
        r = numerator % denominator
        if(r):
            result.append(".") # there would be fraction
        d, count = {}, 2
        while(r != 0 and r not in d):
            d[r] = count
            r *= 10
            while(r < denominator):
                r *= 10
                result.append("0")
                count += 1
            result.append(str(r//denominator))
            count += 1
            r = r % denominator
        if(r):
            result.insert(d[r], "(")
            result.append(")")
        if(int(sign1) ^ int(sign2)):
            result.insert(0, "-")
        return "".join(result)
            
