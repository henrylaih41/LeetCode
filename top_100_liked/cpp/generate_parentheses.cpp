class Solution {
public:
    unordered_map<int, vector<string>> cache;
    Solution(){
        cache[0] = {""};
    }
    
    vector<string> generateParenthesis(int n) {
        if(cache.find(n) != cache.end())
            return cache[n];
        vector<string> result;
        vector<string> internal;
        vector<string> external;
        for(int i = 0; i < n; i++){
            internal = generateParenthesis(i);
            external = generateParenthesis(n-1-i);
            for(auto in : internal)
                for(auto ex: external)
                    result.push_back("(" + in + ")" + ex);
        }
        
        cache[n] = result;
        
        return cache[n];
        
    }
};
