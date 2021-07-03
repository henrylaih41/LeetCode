            return False
        if(s3 == ""):
            if(s2 == "" and s1 == ""):
                return True
            return False
        
        result = False
        if(len(s1) and s3[0] == s1[0]):
            result = result or self.isInterleave(s1[1:], s2, s3[1:])
        if(result == False and len(s2) and s3[0] == s2[0]):
            result = result or self.isInterleave(s1, s2[1:], s3[1:])
            
        return result
    
    def v2isInterleave(self, s1, s2, s3):
        if(len(s1) + len(s2) != len(s3)):
            return False
        if(len(s1) == 0):
            return s2 == s3
        if(len(s2) == 0):
            return s1 == s3
        
        self.memo = {}
        return self.recur(s1, s2, s3, 0, 0)
    
    ### top down recurisve note that k = i + j
    def recur(self, s1, s2, s3, i, j):
        k = i + j
        if((i, j) in self.memo):
            return self.memo[(i, j)]
        
        if(k == len(s3)):
            if(j == len(s2) and i == len(s1)):
                return True
            return False
        
        result = False
        if(i < len(s1) and s3[k] == s1[i]):
            result = result or self.recur(s1, s2, s3, i+1, j)
        if(result == False and j < len(s2) and s3[k] == s2[j]):
            result = result or self.recur(s1, s2, s3, i, j+1)
        self.memo[(i, j)] = result    
        return result
    
    ### bottom-up
    def isInterleave(self, s1, s2, s3):
        if(len(s1) + len(s2) != len(s3)):
            return False
        
        n, m = len(s1), len(s2)
        dp = [[0] * (m+1) for _ in range(2)]
        dp[0][0] = True
        for j in range(1, len(s2)+1):
            dp[0][j] = dp[0][j-1] and (s2[j-1] == s3[j-1])
            
        for i in range(1, len(s1)+1):
            dp[i%2][0] = dp[(i-1)%2][0] and (s1[i-1] == s3[i-1])
            for j in range(1, len(s2)+1):
                dp[i%2][j] = (dp[(i-1)%2][j] and (s3[i+j-1] == s1[i-1])) or (dp[i%2][j-1] and (s3[i+j-1] == s2[j-1]))
                
        return dp[len(s1)%2][len(s2)]
