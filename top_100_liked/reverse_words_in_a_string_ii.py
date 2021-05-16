class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0
        for tail in range(len(s)):
            if(s[tail] == " "):
                self.rs(s, head, tail-1)
                head = tail+1
        self.rs(s, head, len(s)-1)
        self.rs(s, 0, len(s)-1)
        
    def rs(self, s, i, j):
        while(i < j):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
