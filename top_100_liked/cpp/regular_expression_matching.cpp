class Solution {
public:
    vector<vector<int>> memo;
    int n, m;
    // recursive top-down dp
    // if it is a char we must take
    bool isMatch(string s, string p) {
        n = s.length();
        m = p.length();
        memo = vector< vector<int> >(n+1, vector<int>(m+1, -1));
        return (bool)recur(s, p, 0, 0);
    }
    // we need to be able to handle s = "" p = c*b*...
    int recur(string s, string p, int i, int j){
        if(memo[i][j] != -1)
            return memo[i][j];
        
        if(j == m)
            return (i == n);
        
        bool match = (i < n) && (s[i] == p[j] || p[j] == '.');
        
        if(j+1 < m && p[j+1] == '*'){
            memo[i][j] = (match && recur(s, p, i+1, j)) || recur(s, p, i, j+2);
        }
        else{
            memo[i][j] = match && recur(s, p, i+1, j+1);
        }
        
        return memo[i][j];
    }
};
