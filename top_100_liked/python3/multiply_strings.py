class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        num2_int = [int(num2[i]) for i in range(len(num2)-1, -1, -1)]
        for i in range(len(num1)-1, -1, -1):
            n1 = int(num1[i])
            poww = 10 ** (len(num1)-1-i)
            carry = 0
            for n in num2_int:
                summ = n1 * n + carry
                carry = summ // 10
                total += ((summ % 10) * poww)
                poww *= 10
            total += (carry * poww)
        return str(total)
