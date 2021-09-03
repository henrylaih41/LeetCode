class Solution {
public:
    // find k version
    int v1search(vector<int>& nums, int target) {
        // first binary search to find k
        int k, n = nums.size();
        int mid, l = 0, r = n;
        if(nums[n-1] >= nums[0])
            k = 0;
        else{
            while(l < r){
                mid = (r-l)/2 + l;
                if(mid-1 >= 0 && nums[mid] < nums[mid-1]){
                    k = mid;
                    break;
                }
                else{
                    if(nums[mid] < nums[0])
                        r = mid;
                    else
                        l = mid + 1;
                }
            }
        }
        // normal binary search with index-mapping
        l = 0;
        r = n;
        while(l < r){
            mid = (r-l)/2 + l;
            if(nums[(mid + k) % n] == target)
                return (mid + k) % n;
            else if(nums[(mid + k) % n] > target)
                r = mid;
            else
                l = mid + 1;
        }
        return -1;
    }
    // direct search
    int search(vector<int>& nums, int target){
        
    }
};
