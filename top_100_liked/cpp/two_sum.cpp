using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        size_t n = nums.size();
        unordered_map<int, size_t> index_map;
        for(size_t i = 0; i < n; ++i){
            if(index_map.find(target - nums[i]) != index_map.end()){
                return {(int)i, (int)index_map[target - nums[i]]};
            }
            index_map[nums[i]] = i;
        }
        return {};
    }
};
