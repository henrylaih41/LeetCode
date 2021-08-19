class Solution {
public:
    int numSquares(int n) {
        vector<int> squares;
        int root = sqrt(n), level = 0;
        for(int i = 1; i <= root; i++)
            squares.push_back(i * i);
        vector<int> queue;
        queue.push_back(n);
        while(1){
            unordered_set<int> s;
            for(int i = 0; i < queue.size(); i++){
                for(auto sq : squares){
                    int diff = (queue[i] - sq);
                    if(diff > 0)
                        s.insert(diff);
                    else if(diff == 0)
                        return level+1;
                }
            }
            queue.clear();
            for(auto n : s)
                queue.push_back(n);
            level ++;
        }
    }
};
