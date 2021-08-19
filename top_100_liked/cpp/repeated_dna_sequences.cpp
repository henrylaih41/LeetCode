class Solution {
public:
    int powerOf(int base, int x){
        int result = 1;
        for(int i = 0; i < x; ++i)
            result *=  base;
        return result;
    }
    // O(n^2) sliding window through all 10-letter-long, and O(n) search 
    // O(n) rabin-karp algorithm
    vector<string> findRepeatedDnaSequences(string s) {
        // C is the number of characters, L is the substring length 
        vector<string> result;
        int C = 4, L = 10, sum = 0; // since L is 10, the sum would not overflow
        if(s.length() < L) return {};
        map<int, int> count;
        map<char, int> mapping = {{'A', 0}, {'T', 1}, {'C', 2}, {'G', 3}};
        for(int i = 0; i < L; ++i){
            sum *= C;
            sum += mapping[s[i]];
        }
        count[sum] = 1;
        
        for(size_t i = L; i < s.length(); ++i){
            sum -= (mapping[s[i-L]] * powerOf(C, L-1)); 
            sum *= C;
            sum += mapping[s[i]];
            if(count.find(sum) == count.end())
                count[sum] = 1;
            else if(count[sum] == 1){
                result.push_back(s.substr(i - L + 1, L));
                count[sum] += 1;
            }
        }
        
        return result;
    }
};
