        
    def allPalindrome(self, s, intervals):
        for i in range(len(s)):
            ### odd 
            l, r = None, None
            for j in range(len(s)):
                if(i - j < 0 or i + j >= len(s)):
                    break
                if(s[i-j] == s[i+j]):
                    intervals.add((i-j, i+j))
                else:
                    break
                
            ### i-j, i+j+1
            for j in range(len(s)):
                if(i-j < 0 or i+j+1 >= len(s)):
                    break
                if(s[i-j] == s[i+j+1]):
                    intervals.add((i-j, i+j+1))
                else:
                    break
                    
    ### O(N) space version, we construct dp on the fly when expanding on center               
    def minCut(self, s):
        dp = [math.inf] * len(s)
        
        for i in range(len(s)):
            ### odd
            ###      |-> i - j    
            ###      | |-> i + j 
            ### xxxxxaba
            ###     |-> i-j-1
            for j in range(len(s)):
                if(i-j < 0 or i+j >= len(s)):
                    break
                if(s[i-j] == s[i+j]):
                    left_dp = 0 if(i-j-1 < 0) else dp[i-j-1]
                    dp[i+j] = min(left_dp+1, dp[i+j])
                else:
                    break
            ### even
            ###      |-> i - j
            ###      |  |-> i + j + 1
            ### xxxxxadda
            ###     | |-> i
            ###     |-> i-j-1
            for j in range(len(s)):
                if(i+j+1 >= len(s) or i-j < 0):
                    break
                if(s[i+j+1] == s[i-j]):
                    left_dp = 0 if(i-j-1 < 0) else dp[i-j-1]
                    dp[i+j+1] = min(left_dp+1, dp[i+j+1])
                else:
                    break
            
        return dp[-1] - 1
