class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        num1, num2 = 0, 0
        i = 0
        while(i < len(v1) or i < len(v2)):
            if(i >= len(v1)):
                num1 = 0
            else:
                num1 = int(v1[i])
            if(i >= len(v2)):
                num2 = 0
            else:
                num2 = int(v2[i])
            if(num1 > num2):
                return 1
            if(num1 < num2):
                return -1
            i += 1
        
        return 0
