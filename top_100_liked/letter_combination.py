class Solution:
    def solve(self, digits, d):
        result = []
        # base case
        if(len(digits) == 1):
            for c in d[digits[0]]:
                result.append(c)
            return result
        sss = self.solve(digits[1:], d)
        for c in d[digits[0]]:
            for ss in sss:
                result.append(c + ss)
        return result

    def letterCombinations(self, digits: str) -> List[str]:
        d = {"1": "",
             "2": "abc",
             "3": "def",
             "4": "ghi",
             "5": "jkl",
             "6": "mno",
             "7": "pqrs",
             "8": "tuv",
             "9": "wxyz"}
        # edge case
        if(len(digits) == 0):
            return []
        return self.solve(digits, d)

