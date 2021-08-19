class Solution {
public:
    // size of nums, range of nums[i]
    // use two sums as subroutine
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int> > result;
        int i = 0, n = nums.size();
        while(i < n){
            // early stopping
            if(nums[i] > 0)
                break;
            twoSum(nums, nums[i], i+1, n-1, -nums[i], result);
            int prev = nums[i];
            while(i < n && nums[i] == prev)
                i++;
        }
        
        return result;
    }
    
    void twoSum(vector<int>& num, int k, int start, int end, int target, vector<vector<int> >& result){
        int l = start, r = end;
        
        while(l < r){
            int sum = num[l] + num[r];
            if(sum < target)
                l++;
            else if(sum > target)
                r--;
            else{
                result.push_back({k, num[l], num[r]});
                int prev = num[l];
                while(l < r && num[l] == prev)
                    l ++;
            }
        }
    }
};
