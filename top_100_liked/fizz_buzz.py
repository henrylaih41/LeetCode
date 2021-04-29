class Solution:
    ### 40ms
    def v1fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            word = []
            if(i % 3 == 0):
                word.append("Fizz")
            if(i % 5 == 0):
                word.append("Buzz")
            if(len(word) == 0):
                word.append(str(i))
            result.append("".join(word))
        return result
    ### 28~40ms
    def v2fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            w = ""
            if(i % 3 == 0):
                w += "Fizz"
            if(i % 5 == 0):
                w += "Buzz"
            if(w == ""):
                w = str(i)
            result.append(w)
        return result
    ### 40ms
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            if(i % 15 == 0):
                result.append("FizzBuzz")
            elif(i % 3 == 0):
                result.append("Fizz")
