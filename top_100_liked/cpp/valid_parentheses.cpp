class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, int> m = {
            {'(', 1}, 
            {')', -1}, 
            {'{', 2}, 
            {'}', -2},
            {'[', 3},
            {']', -3}
        };
        
        vector<char> stack;
        int n = s.length();
        for(int i = 0; i < n; i++){
            // left bracket
            if(m[s[i]] > 0){
                stack.push_back(s[i]);
            }
            // right bracket
            else{
                // unmatch
                if(stack.size() == 0)
                    return false;
                if(m[stack.back()] + m[s[i]] != 0)
                    return false;
                else{
                    stack.pop_back();
                }
            }
        }
        
        return (stack.size() == 0);
    }
};
