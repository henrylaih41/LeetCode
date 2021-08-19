class TwoSum {
public:
    map<int, int> mapp;
    /** Initialize your data structure here. */
    TwoSum() {
        
    }
    
    /** Add the number to an internal data structure.. */
    void add(int number) {
        if(mapp.find(number) != mapp.end())
            mapp[number] += 1;
        else
            mapp[number] = 1;
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
       
        for(auto p : mapp){     
            long target = (long)value - (long)p.first;
            if(target > INT_MAX || target < INT_MIN)
                continue;
            if(mapp.find(value - p.first) != mapp.end()){
                // if there are not enough element in mapp 
                if(p.first == value - p.first && p.second == 1)
                   continue;
                return true;
            }
               
        }
        return false;
    }
};
​
/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */
