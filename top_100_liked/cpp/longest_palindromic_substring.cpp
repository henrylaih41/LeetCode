class Solution {
public:
    struct sub_index{
        size_t i, j;    
    };
    
    string longestPalindrome(string s) {
        //return expandFromCenter(s); 
        return dynamicProgramming(s);
    }
    
    string expandFromCenter(string s){
        size_t maxx = 0;
        sub_index ans;
        // odd center
        size_t s_len = s.length();
        for(size_t i = 0; i < s_len; ++i){
            for(size_t j = 0; j < s_len; ++j){
                if(i < j || (i + j) >= s_len)
                    break;
                if(s[i-j] != s[i+j])
                    break;
                else if(2*j + 1 > maxx){
                    maxx = 2 * j + 1;
                    ans.i = i - j;
                    ans.j = i + j;
                }
            }
        }
        // even center
        for(size_t i = 0; i < s_len; ++i){
            for(size_t j = 0; j < s_len; ++j){
                if(i < j || (i + j + 1) >= s_len)
                    break;
                if(s[i-j] != s[i+j+1])
                    break;
                else if(2*j + 2 > maxx){
                    maxx = 2*j + 2;
                    ans.i = i - j;
                    ans.j = i + j + 1;
                }
            }
        }
                
        return s.substr(ans.i, ans.j - ans.i + 1);
    }
    
    string dynamicProgramming(string s){
        size_t n = s.length(), maxx = 0;
        sub_index ans;
        int dp[n][n];
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j)
                dp[i][j] = 0;
        
        ans.i = 0;
        ans.j = 0;
        // init dp table
