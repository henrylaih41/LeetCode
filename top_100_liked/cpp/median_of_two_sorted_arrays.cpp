class Solution {
public:
    // binary search, handle the edge case (think carefully of the out of bound cases)
    // be careful of the range of the binary search (r is n+1)
    double findMedianSortedArrays(vector<int>& a, vector<int>& b) {
        // ensure a is the longer array
        if(a.size() < b.size())
            return findMedianSortedArrays(b, a);
        int i, j, u, u_, d, d_, l = 0, r = a.size() + 1;
        int split = (a.size() + b.size()) / 2;
        bool odd = (a.size() + b.size()) % 2;
        // do binary search on a
        while(l < r){
            i = (l + r) / 2;
            j = split - i;
            // this means that we choose too right in a
            if(j < 0){
                r = i;
                continue;
            }
            // this means we choose to left in a
            if(j > b.size()){
                l = i+1;
                continue;
            }
            u  = (i < a.size()) ? a[i] : INT_MAX;
            u_ = (i-1 >= 0) ? a[i-1] : INT_MIN;
            d  = (j < b.size()) ? b[j] : INT_MAX;
            d_ = (j-1 >= 0) ? b[j-1] : INT_MIN;
            
            if(u >= d_ && d >= u_){
                if(odd) return min(d, u);
                else return (min(d, u) + max(d_, u_))/2.0;
            }
            // [..., u_, u, ...]
            // [..., d_, d, ...]
            else if(d_ > u){
                l = i+1;
            } 
            else if(u_ > d){
                r = i;
            }
        }
        
        return 0;
​
    }
};
