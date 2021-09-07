class Solution:
    def canWinNim(self, n: int) -> bool:
        if(n <= 3):
            return True
        return (n % 4)
