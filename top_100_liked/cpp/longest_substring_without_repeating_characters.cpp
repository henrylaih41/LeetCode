class Solution {
public:
    // hash_map tends to be slow, we can use array or vector for best speed
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> mapp;
        int head = 0, tail = 0, len_s = s.length();
        int maxx = 0;
        while(tail < len_s){
            if(mapp.find(s[tail]) != mapp.end()){
                mapp.erase(mapp.find(s[head]));
                head ++;
            }
            else{
                mapp.insert(s[tail]);
                maxx = max(tail - head + 1, maxx);
                tail ++;
            }
        }
        return maxx;
    }
};
