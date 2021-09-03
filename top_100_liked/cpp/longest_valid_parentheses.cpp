class Solution {
public:
    // we cannot use expand center to do this problem
    // brute force takes O(n^2)
    // stack method (we observe that a least valid parentheses (not concat) has a property which
    // is no other valid parentheses can start within it), so we can use a stack a greedly search for
    // the longest least valid, and concat them together
    int longestValidParentheses(string s) {
        vector<int> stack;
        int n = s.size(), prev = -1, maxx = 0;
        stack.push_back(prev);
        for(int i = 0; i < n; i++){
            if(s[i] == '(')
                stack.push_back(i);
            else{
                stack.pop_back();
                if(stack.empty())
                    stack.push_back(i);
                else
                    maxx = max(maxx, i - stack.back());
            }
        }
        
        return maxx;
    };
};
