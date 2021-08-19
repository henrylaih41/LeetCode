class Solution {
public:
    // solve it recursively
    unordered_map<char, string> m = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
    
    vector<string> letterCombinations(string digits) {
        if(digits == "")
            return {};
        vector<string> result;
        char k = digits[0];
        string ss = m[k];
        int n = ss.length();
        vector<string> next = letterCombinations(digits.substr(1));
        if(next.size() == 0)
            next = {""};
        for(int i = 0; i < n; i++){
            for(string s : next)
                result.push_back(ss[i] + s);
        }
        
        return result;
    }
};
