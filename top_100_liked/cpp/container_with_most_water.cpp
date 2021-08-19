#include <algorithm>
class Solution {
public:
    // size of height, range of element in height
    // we use two pointer technique, start from both ends.
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        long long result = min(height[l], height[r]) * (r - l);
        while(l < r){
            if(height[l] <= height[r]){
                int tmp = height[l];
                while(height[l] <= tmp && l < r)
                    l ++;
            }
            else{
                int tmp = height[r];
                while(height[r] <= tmp && l < r)
                    r --;
            }
            result = max(result, (long long)min(height[l], height[r]) * (long long)(r - l));
        }
        
        return result;
    }
};
